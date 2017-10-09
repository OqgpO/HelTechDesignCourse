# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-09 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('introduction', models.TextField(max_length=2000)),
                ('portrait', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
