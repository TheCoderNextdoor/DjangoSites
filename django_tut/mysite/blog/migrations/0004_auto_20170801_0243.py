# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170801_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='mood',
            field=models.TextField(null=True),
        ),
    ]
