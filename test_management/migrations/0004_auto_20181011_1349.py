# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-11 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_management', '0003_auto_20181011_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='img_option',
            field=models.FileField(blank=True, null=True, upload_to='question_options'),
        ),
    ]
