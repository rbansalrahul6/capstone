# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_name', models.CharField(unique=True, max_length=255)),
                ('branch_code', models.CharField(max_length=255, serialize=False, primary_key=True)),
            ],
            options={
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_name', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('short_name', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
