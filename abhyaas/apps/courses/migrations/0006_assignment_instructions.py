# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20171212_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='instructions',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
