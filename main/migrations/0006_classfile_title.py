# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20161213_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='classfile',
            name='title',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
