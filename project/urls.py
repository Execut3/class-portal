# -*- coding: utf-8 -*-
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.templatetags.static import static

from main.views import *
from project import settings

urlpatterns = [
    url("^admin/", include(admin.site.urls)),
    url(r'^captcha', include('captcha.urls')),
    # url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^login$', login_view, name='login'),
    url(r'^logout$', logout_view, name='logout'),
    url(r'^register$', register_view, name='register'),
    url(r'^$', index, name='root'),
    url(r'^index$', index, name='index'),
    url(r'^change-password$', change_password, name='change_password'),
    url(r'^main-content/(?P<id>\d+)$', main_content, name='main_content'),
    url(r'^session/(?P<id>\d+)$', class_session, name='class_session'),
    url(r'^scoreboard$', scoreboard, name='scoreboard'),

    url(r'^tasks/main$', total_tasks, name='total_tasks'),
    url(r'^tasks/view/(?P<task_id>\d+)/$', task_view, name='task'),
    url(r'^tasks/submit$', submit_task, name='submit_task'),
    url(r'^tasks/last-submits$', last_submits, name='last_submits'),
]

urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )
