# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-10-28 13:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loader', '0010_tickets'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tickets',
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
