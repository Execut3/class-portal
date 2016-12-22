# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_taskresult_received_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('content', ckeditor.fields.RichTextField(null=True, blank=True)),
                ('file', models.FileField(null=True, upload_to=main.models.file_upload_dir, blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
