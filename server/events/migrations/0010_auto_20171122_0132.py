# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20171114_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='speaker',
        ),
        migrations.AddField(
            model_name='event',
            name='punchline',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]