# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_eventworker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventworker',
            name='update_freq',
        ),
        migrations.AddField(
            model_name='eventworker',
            name='page_name',
            field=models.CharField(default='testpage', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eventworker',
            name='user_token',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='eventworker',
            name='page_token',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]