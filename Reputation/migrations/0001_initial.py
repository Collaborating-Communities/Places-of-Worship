# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-17 17:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('BasicArticle', '0020_merge_20180627_1228'),
        ('Community', '0028_communitymedia'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleScoreLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvote', models.IntegerField(default=0, null=True)),
                ('downvote', models.IntegerField(default=0, null=True)),
                ('reported', models.IntegerField(default=0, null=True)),
                ('publish', models.BooleanField(default=False)),
                ('resource', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BasicArticle.Articles')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleUserScoreLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvoted', models.BooleanField(default=False)),
                ('downvoted', models.BooleanField(default=False)),
                ('reported', models.BooleanField(default=False)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicArticle.Articles')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommunityReputaion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(null=True)),
                ('community', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Community.Community')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_vote_unpublished', models.BooleanField(default=True)),
                ('upvote_value', models.IntegerField(null=True)),
                ('downvote_value', models.IntegerField(null=True)),
                ('can_report', models.BooleanField(default=True)),
                ('publish_value', models.IntegerField(null=True)),
                ('resource_type', models.CharField(default='resource', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.IntegerField(null=True)),
                ('publisher', models.IntegerField(null=True)),
                ('role_score', models.CharField(default='role_score', max_length=20)),
            ],
        ),
    ]
