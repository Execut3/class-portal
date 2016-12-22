# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20161213_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskresult',
            name='title',
            field=models.CharField(default=b'', max_length=50),
        ),
    ]
