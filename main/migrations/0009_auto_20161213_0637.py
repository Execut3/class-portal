# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_taskresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, null=True, blank=True)),
                ('content', ckeditor.fields.RichTextField(null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='classsession',
            name='content',
        ),
        migrations.AddField(
            model_name='classcontent',
            name='session',
            field=models.ForeignKey(to='main.ClassSession'),
        ),
    ]
