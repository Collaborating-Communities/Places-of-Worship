# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-18 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reputation', '0003_badgescore'),
    ]

    operations = [
        migrations.AddField(
            model_name='communityreputaion',
            name='published_by_me_count',
            field=models.IntegerField(default=0),
        ),
    ]