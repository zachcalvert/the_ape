# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-05 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_audiowidget'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiowidget',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]