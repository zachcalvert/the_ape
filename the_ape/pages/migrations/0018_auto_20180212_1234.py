# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-12 20:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20180212_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventfocuswidget',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event'),
        ),
        migrations.AlterField(
            model_name='personfocuswidget',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Person'),
        ),
    ]