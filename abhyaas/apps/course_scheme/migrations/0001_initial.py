# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_code', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('course_name', models.CharField(max_length=20)),
            ],
        ),
    ]
