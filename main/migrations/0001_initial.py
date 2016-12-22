# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64, verbose_name=b'\xd9\x86\xd8\xa7\xd9\x85 \xd8\xaa\xdb\x8c\xd9\x85')),
                ('description', models.TextField(max_length=1024, verbose_name=b'\xd8\xaa\xd9\x88\xd8\xb6\xdb\x8c\xd8\xad\xd8\xa7\xd8\xaa \xd8\xaf\xd8\xb1 \xd9\x85\xd9\x88\xd8\xb1\xd8\xaf \xd8\xaa\xdb\x8c\xd9\x85')),
                ('score', models.PositiveIntegerField(default=0, verbose_name=b'\xd8\xa7\xd9\x85\xd8\xaa\xdb\x8c\xd8\xa7\xd8\xb2')),
                ('logo', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(to='main.Team'),
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
