# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-17 11:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awwardsmain', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
