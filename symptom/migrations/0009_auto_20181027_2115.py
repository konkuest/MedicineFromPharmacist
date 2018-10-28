# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-27 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symptom', '0008_auto_20181027_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='bodypart',
            name='ques_f',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bodypart',
            name='ques_g',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bodypart',
            name='ques_h',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bodypart',
            name='ques_i',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bodypart',
            name='ques_j',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bodypart',
            name='ques_k',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bodypart',
            name='ques_l',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bodypart',
            name='ques_m',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='bodypart',
            name='partname',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='bodypart',
            name='ques_a',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='bodypart',
            name='ques_b',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='bodypart',
            name='ques_c',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='bodypart',
            name='ques_d',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='bodypart',
            name='ques_e',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
