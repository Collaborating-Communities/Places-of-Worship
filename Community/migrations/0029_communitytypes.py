# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-11-01 07:42
from __future__ import unicode_literals

import Community.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Community', '0028_communitymedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to=Community.models.get_file_path)),
            ],
        ),
    ]