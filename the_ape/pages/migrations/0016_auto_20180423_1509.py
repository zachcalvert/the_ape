# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-23 22:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20180423_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videoswidget',
            old_name='video_clips',
            new_name='videos',
        ),
    ]
