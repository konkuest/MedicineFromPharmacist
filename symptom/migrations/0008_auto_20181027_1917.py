# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-27 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symptom', '0007_auto_20181027_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bodypart',
            name='subquestions',
        ),
        migrations.AddField(
            model_name='bodypart',
            name='ques_a',
            field=models.CharField(default='Qs', max_length=100),
        ),
        migrations.AddField(
            model_name='bodypart',
            name='ques_b',
            field=models.CharField(default='Qs', max_length=100),
        ),
        migrations.AddField(
            model_name='bodypart',
            name='ques_c',
            field=models.CharField(default='Qs', max_length=100),
        ),
        migrations.AddField(
            model_name='bodypart',
            name='ques_d',
            field=models.CharField(default='Qs', max_length=100),
        ),
        migrations.AddField(
            model_name='bodypart',
            name='ques_e',
            field=models.CharField(default='Qs', max_length=100),
        ),
    ]
