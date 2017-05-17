# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 20:25
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Venue')),
            ],
        ),
    ]