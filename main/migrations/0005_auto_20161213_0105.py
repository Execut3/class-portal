# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20161213_0104'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=main.models.file_upload_dir, blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('session', models.ForeignKey(to='main.ClassSession')),
            ],
        ),
        migrations.RemoveField(
            model_name='classfiles',
            name='session',
        ),
        migrations.DeleteModel(
            name='ClassFiles',
        ),
    ]
