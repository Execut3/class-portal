# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_taskresult_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taskresult',
            options={'ordering': ['-submit_time']},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['-score']},
        ),
        migrations.AddField(
            model_name='taskresult',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
