# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-16 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20161216_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='lessons_completed',
            field=models.ManyToManyField(to='courses.Exercise'),
        ),
    ]