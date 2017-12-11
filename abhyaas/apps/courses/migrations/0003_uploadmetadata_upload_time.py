# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_uploadmetadata'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadmetadata',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 10, 21, 6, 34, 821094)),
            preserve_default=False,
        ),
    ]
