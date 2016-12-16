# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-16 13:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20161216_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='next_exercise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next', to='courses.Exercise'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='prev_exercise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prev', to='courses.Exercise'),
        ),
    ]