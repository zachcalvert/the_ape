# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-11 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20180207_1153'),
        ('people', '0009_houseteam_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='houseteam',
            name='videos',
            field=models.ManyToManyField(blank=True, null=True, to='pages.VideoWidget'),
        ),
        migrations.AlterField(
            model_name='person',
            name='videos',
            field=models.ManyToManyField(blank=True, null=True, to='pages.VideoWidget'),
        ),
    ]