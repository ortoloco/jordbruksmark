# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-17 21:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jordbruksmark', '0003_auto_20161217_2150'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Wochen_Menge',
            new_name='WochenMenge',
        ),
    ]
