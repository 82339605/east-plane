# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-10-31 15:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loader', '0017_ticket'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ticket',
        ),
    ]
