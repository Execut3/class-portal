# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_maincontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='description',
            field=models.TextField(max_length=1024, null=True, verbose_name=b'\xd8\xaa\xd9\x88\xd8\xb6\xdb\x8c\xd8\xad\xd8\xa7\xd8\xaa \xd8\xaf\xd8\xb1 \xd9\x85\xd9\x88\xd8\xb1\xd8\xaf \xd8\xaa\xdb\x8c\xd9\x85', blank=True),
        ),
    ]
