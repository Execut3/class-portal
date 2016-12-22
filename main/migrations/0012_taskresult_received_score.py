# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20161213_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskresult',
            name='received_score',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
