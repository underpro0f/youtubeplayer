# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-10 17:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialprofile', '0002_socialprofile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialprofile',
            name='avatar',
        ),
    ]
