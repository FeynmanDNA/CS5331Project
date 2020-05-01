# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-01 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20200413_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='formaction',
            field=models.TextField(default='form action'),
        ),
        migrations.AddField(
            model_name='article',
            name='iframe_src',
            field=models.TextField(default='iframe-src'),
        ),
        migrations.AddField(
            model_name='article',
            name='math_href',
            field=models.TextField(default='math href'),
        ),
        migrations.AlterField(
            model_name='article',
            name='author_homepage',
            field=models.TextField(default='#', max_length=200),
        ),
        migrations.AlterField(
            model_name='article',
            name='imgSize',
            field=models.TextField(default='smallIMG', max_length=200),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_color',
            field=models.TextField(default='blue', max_length=200),
        ),
    ]
