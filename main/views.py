# -*- coding: utf-8 -*-
import os

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.translation import ugettext as _

from main.forms import LoginForm, RegisterForm, SubmitResultForm, ChangePasswordForm
from main.models import ClassSession, ClassFile, Task, Player, TaskResult, Team, MainContent, ClassContent
from project.settings import BASE_DIR

from django.utils import timezone


@login_required(login_url='login')
def index(request):
    class_sessions = ClassSession.objects.all()
    main_contents = MainContent.objects.all()
    return render_to_response('index.html', locals(), RequestContext(request))


@login_required(login_url='login')
def change_password(request, **kwargs):
    if not request.method == 'POST':
        change_password_form = ChangePasswordForm()
        return render_to_response('change_password.html', locals(), RequestContext(request))

    change_password_form = ChangePasswordForm(request.POST)
    if change_password_form.is_valid():
        current_password = change_password_form.cleaned_data['current_password']
        new_password = change_password_form.cleaned_data['new_password']
        new_password_confirm = change_password_form.cleaned_data['new_password_confirm']

        if new_password != new_password_confirm:
            error = 'پسوردهای وارد شده تطابق نداشتند.'
        else:
            user = authenticate(username=request.user.username, password=current_password)
            if user:
                user = request.user
                user.set_password(new_password)
                user.save()
                success = 'پسورد با موفقیت تغییر یافت.'
            else:
                error = 'پسورد فعلی به درستی وارد نشده است.'
    return render_to_response('change_password.html', locals(), RequestContext(request))


def main_content(request, **kwargs):
    id = kwargs.pop('id', 1)
    main_content = MainContent.objects.filter(id=id).first()
    return render_to_response('main_content.html', locals(), RequestContext(request))


@login_required(login_url='login')
def scoreboard(request):
    teams = Team.objects.all()
    team_list = []
    for team in teams:
        team_list.append({'team': team, 'players': Player.objects.filter(team=team)})
    return render_to_response('scoreboard.html', locals(), RequestContext(request))


def login_view(request, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))

    if not request.method == 'POST':
        login_form = LoginForm()
        return render_to_response('login.html', locals(), RequestContext(request))

    messages = {'success': '', 'error': ''}
    login_form = LoginForm(request.POST)
    if login_form.is_valid():
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            messages['error'] = _('Not a registered user.')
    else:
        print login_form.errors
        messages['error'] = _('Please fill form correctly.')
    print messages
    return render_to_response('login.html', locals(), RequestContext(request))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def register_view(request, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))

    if not request.method == 'POST':
        register_form = RegisterForm()
        return render_to_response('register.html', locals(), RequestContext(request))

    register_form = RegisterForm(request.POST)
    if register_form.is_valid():
        username = register_form.cleaned_data['username']
        first_name = register_form.cleaned_data['first_name']
        last_name = register_form.cleaned_data['last_name']
        email = register_form.cleaned_data['email']
        password = register_form.cleaned_data['password']

        is_registered_user = User.objects.filter(Q(username=username) | Q(email=email)).exists()
        if is_registered_user:
            error = 'کاربری با این مشخصات قبلا در سامانه ثبت‌نام نموده است.'
        else:
            user = User.objects.create(username=username, email=email)
            print user
            user.set_password(password)
            user.is_active = True
            user.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        error = 'لطفا اطلاعات درخواستی را به درستی وارد نمایید.'

    return render_to_response('register.html', locals(), RequestContext(request))


def class_session(request, **kwargs):
    id = kwargs.pop('id', 0)
    if id == 0:
        raise Http404
    session = get_object_or_404(ClassSession, pk=id)
    files = ClassFile.objects.filter(session=session)
    contents = ClassContent.objects.filter(session=session)
    return render_to_response('class_session.html', locals(), RequestContext(request))


@login_required(login_url='login')
def total_tasks(request):
    tasks = Task.objects.filter(active=True)
    return render_to_response('tasks.html', locals(), RequestContext(request))


@login_required(login_url='login')
def task_view(request, **kwargs):
    id = kwargs.pop('task_id', 0)
    if id == 0:
        raise Http404
    task = get_object_or_404(Task, pk=id, active=True)
    is_finished = timezone.now() > task.deadline or task.closed

    submit_result_form = SubmitResultForm()
    task_results = TaskResult.objects.filter(team__player__user=request.user, task=task)
    return render_to_response('task_view.html', locals(), RequestContext(request))


@login_required(login_url='login')
def submit_task(request, **kwargs):
    player = get_player_profile(request.user)
    team = player.team
    # if not team:
    #     print 'no team profile for user'
    #     return HttpResponseRedirect(reverse('total_tasks'))
    id = request.POST.get('task_id', '')
    print id
    task = get_object_or_404(Task, pk=id)

    if not request.method == 'POST' or not team:
        return HttpResponseRedirect(reverse('task_view', kwargs={'task_id': task.id}))

    submit_result_form = SubmitResultForm(request.POST)
    if submit_result_form.is_valid():
        title = submit_result_form.cleaned_data['title']
        content = submit_result_form.cleaned_data['content']
        task_result, created = TaskResult.objects.get_or_create(task=task, team=team, title=title,
                                                                content=content)
        print task_result
    return HttpResponseRedirect(reverse('task', kwargs={'task_id': task.id}))


def last_submits(request):
    submits = TaskResult.objects.all()[:50]
    return render_to_response('last_submits.html', locals(), RequestContext(request))


def get_player_profile(user):
    return get_object_or_404(Player, user=user)


def update_database():
    users_list = open(os.path.join(BASE_DIR, 'users.list'), 'r').readlines()
    for u in users_list:
        username = u.split(',')[0]
        email = u.split(',')[1]
        user = User.objects.create(username=username, email=email)
        user.set_password('12345678')
        user.save()
        print user