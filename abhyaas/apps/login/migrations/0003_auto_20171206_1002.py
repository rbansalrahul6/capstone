# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20171124_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='sem',
        ),
        migrations.AddField(
            model_name='student',
            name='batch',
            field=models.IntegerField(default=2014, choices=[(2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='semester',
            field=models.IntegerField(default=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]),
        ),
    ]
