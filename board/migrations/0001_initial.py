# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-01-30 03:45
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='제목')),
                ('subject', models.IntegerField(verbose_name='종류')),
                ('content', ckeditor.fields.RichTextField(verbose_name='내용')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='생성일자')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='수정일자')),
                ('view_count', models.IntegerField(default=0, verbose_name='조회수')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
    ]
