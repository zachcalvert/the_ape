# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-22 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApeClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('bio', models.TextField()),
                ('class_type', models.CharField(choices=[('IMPROV', 'Improv'), ('SKETCH', 'Sketch'), ('ACTING', 'Acting')], max_length=50)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('num_sessions', models.IntegerField(default=4, help_text='Number of Sessions')),
                ('max_enrollment', models.IntegerField(default=12, help_text='Max number of students')),
                ('enrollment_opens', models.DateField(blank=True, null=True)),
                ('enrollment_closes', models.DateField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'verbose_name': 'Ape Class',
                'verbose_name_plural': 'Ape Classes',
            },
        ),
    ]
