# coding=utf-8
# Generated by Django 2.0.1 on 2018-01-29 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_auto_20171123_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaker',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='speakers', to='events.Event'),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='organisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.Organisation'),
        ),
    ]
