# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interpreter', '0006_auto_20170222_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestfly',
            name='cachekiller',
            field=models.CharField(blank=True, default=b'na', max_length=200),
        ),
    ]
