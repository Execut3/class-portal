# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_task_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(null=True, upload_to=main.models.file_upload_dir, blank=True)),
                ('submit_time', models.DateTimeField(auto_now_add=True)),
                ('content', ckeditor.fields.RichTextField(null=True, blank=True)),
                ('task', models.ForeignKey(to='main.Task')),
                ('team', models.ForeignKey(to='main.Team')),
            ],
        ),
    ]
