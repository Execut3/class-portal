# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_settings'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassFiles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=main.models.file_upload_dir, blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClassSession',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, null=True, blank=True)),
                ('content', ckeditor.fields.RichTextField(null=True, blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=main.models.file_upload_dir)),
                ('title', models.CharField(default=b'', max_length=100)),
                ('description', ckeditor.fields.RichTextField(null=True, blank=True)),
                ('closed', models.BooleanField(default=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField(null=True, blank=True)),
                ('score', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='classfiles',
            name='session',
            field=models.ForeignKey(to='main.ClassSession'),
        ),
    ]
