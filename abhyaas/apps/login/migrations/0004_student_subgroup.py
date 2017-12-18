# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20171206_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='subgroup',
            field=models.CharField(default='COE-1', max_length=8),
            preserve_default=False,
        ),
    ]
