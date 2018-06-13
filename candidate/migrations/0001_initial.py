# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-13 04:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=120, null=True)),
                ('firstname', models.CharField(blank=True, max_length=120, null=True)),
                ('lastname', models.CharField(blank=True, max_length=120, null=True)),
                ('phonenumber', models.CharField(blank=True, max_length=120, null=True)),
                ('country', models.CharField(blank=True, max_length=120, null=True)),
                ('file', models.ImageField(blank=True, upload_to=b'profile_image')),
                ('image', models.ImageField(blank=True, upload_to=b'card_image')),
                ('birthday', models.DateField()),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('sname', models.CharField(blank=True, max_length=300, null=True)),
                ('city', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]