# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_scheme', '0004_auto_20171116_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursescheme',
            name='batch',
            field=models.CharField(max_length=5, choices=[(2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016)]),
        ),
    ]
