# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-19 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
