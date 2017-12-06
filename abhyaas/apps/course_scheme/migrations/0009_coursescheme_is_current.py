# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_scheme', '0008_auto_20171124_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursescheme',
            name='is_current',
            field=models.BooleanField(default=False),
        ),
    ]
