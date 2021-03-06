# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 11:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20171114_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attending_count',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='cover_uri',
            field=models.URLField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(blank=True, verbose_name='date organised'),
        ),
        migrations.AlterField(
            model_name='event',
            name='programme',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='event',
            name='speaker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.Speaker'),
        ),
    ]
