# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_scheme', '0002_auto_20171124_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursescheme',
            name='branch',
            field=models.ForeignKey(to='college.Branch'),
        ),
        migrations.AlterField(
            model_name='coursescheme',
            name='semester',
            field=models.IntegerField(default=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]),
        ),
    ]
