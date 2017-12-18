# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_assignment_upload_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadmetadata',
            name='upload_date',
        ),
        migrations.AddField(
            model_name='uploadmetadata',
            name='upload_time',
            field=models.DateField(default=datetime.datetime(2017, 12, 16, 11, 42, 30, 328051, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
