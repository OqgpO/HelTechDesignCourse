# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 08:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20171122_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('streetaddr', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='eventworker',
            name='parse_speakers',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Place'),
        ),
    ]