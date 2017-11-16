# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_scheme', '0005_auto_20171116_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursescheme',
            name='batch',
            field=models.CharField(max_length=5, choices=[(b'2014', b'2014'), (b'2015', b'2015'), (b'2016', b'2016'), (b'2017', b'2017')]),
        ),
    ]
