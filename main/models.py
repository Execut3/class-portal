# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


def file_upload_dir(instance, filename):
    upload_dir = "files/%s" % filename
    return upload_dir


class Team(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='نام تیم')
    description = models.TextField(max_length=1024, verbose_name='توضیحات در مورد تیم', null=True, blank=True)
    score = models.PositiveIntegerField(default=0, verbose_name='امتیاز')
    logo = models.ImageField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-score']


class PlayerManager(models.Manager):
    use_for_related_fields = True


class Player(models.Model):
    user = models.OneToOneField(User)
    team = models.ForeignKey(Team)

    objects = PlayerManager()

    def __unicode__(self):
        return self.user.username


class Setting(models.Model):
    registration_is_open = models.BooleanField(default=True)


class ClassSession(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class ClassFile(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    session = models.ForeignKey(ClassSession)
    file = models.FileField(upload_to=file_upload_dir, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class ClassContent(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    session = models.ForeignKey(ClassSession)
    content = RichTextField(null=True, blank=True)

    def __unicode__(self):
        return self.title


class Task(models.Model):
    file = models.FileField(upload_to=file_upload_dir, null=True, blank=True)
    title = models.CharField(default='', max_length=100)
    description = RichTextField(blank=True, null=True)
    closed = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    score = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title


class TaskResult(models.Model):
    task = models.ForeignKey(Task)
    file = models.FileField(upload_to=file_upload_dir, null=True, blank=True)
    team = models.ForeignKey(Team)
    submit_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, default='')
    content = RichTextField(null=True, blank=True)
    status = models.BooleanField(default=False)
    received_score = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return '%s, %s, %s' % (self.task.title, self.team.name, self.submit_time)

    class Meta:
        ordering = ['-submit_time']


class MainContent(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField(null=True, blank=True)
    file = models.FileField(null=True, blank=True, upload_to=file_upload_dir)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title



