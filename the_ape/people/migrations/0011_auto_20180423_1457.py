# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-23 21:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0010_auto_20180423_1456'),
    ]

    operations = [
        migrations.RenameField(
            model_name='houseteam',
            old_name='video_clips',
            new_name='videos',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='video_clips',
            new_name='videos',
        ),
    ]
