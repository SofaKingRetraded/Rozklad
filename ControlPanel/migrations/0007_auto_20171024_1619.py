# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-24 13:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ControlPanel', '0006_auto_20171023_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimetableInGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ControlPanel.Group')),
            ],
            options={
                'verbose_name': 'Розклад уроків',
                'verbose_name_plural': 'ВИвід',
            },
        ),
        migrations.AlterModelOptions(
            name='timetable',
            options={'verbose_name': 'Розклад уроків', 'verbose_name_plural': 'Створити розклад уроків для класу'},
        ),
        migrations.AddField(
            model_name='timetableingroup',
            name='timetable',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ControlPanel.Timetable'),
        ),
    ]
