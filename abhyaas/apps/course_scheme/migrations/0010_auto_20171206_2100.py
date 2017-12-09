# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_scheme', '0009_coursescheme_is_current'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursescheme',
            name='is_current',
        ),
        migrations.AddField(
            model_name='courseitem',
            name='is_current',
            field=models.BooleanField(default=False),
        ),
    ]
