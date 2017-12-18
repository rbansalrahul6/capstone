# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_uploadmetadata_upload_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='upload_date',
            field=models.DateField(default=datetime.date(2017, 12, 16), auto_now_add=True),
            preserve_default=False,
        ),
    ]
