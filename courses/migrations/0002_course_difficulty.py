# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='difficulty',
            field=models.CharField(default='easy', max_length=20),
            preserve_default=False,
        ),
    ]
