# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-02 04:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='password',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]