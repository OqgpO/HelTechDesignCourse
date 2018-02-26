# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20171009_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='logo',
            field=models.ImageField(upload_to='organisation_logos/'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='portrait',
            field=models.ImageField(upload_to='speaker_portraits/'),
        ),
    ]
