# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-26 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0007_donationsemailsettings_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='source',
            field=models.CharField(choices=[('p', 'paypal'), ('s', 'stripe')], default='p', max_length=2),
        ),
    ]