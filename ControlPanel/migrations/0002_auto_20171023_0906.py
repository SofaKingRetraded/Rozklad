# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-23 06:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ControlPanel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayInGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('day_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ControlPanel.Day')),
                ('group_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ControlPanel.Group')),
            ],
            options={
                'verbose_name': 'День навчання в групі',
                'verbose_name_plural': 'Дні навчання в групах',
            },
        ),
        migrations.RenameModel(
            old_name='Lesson',
            new_name='LessonName',
        ),
    ]
