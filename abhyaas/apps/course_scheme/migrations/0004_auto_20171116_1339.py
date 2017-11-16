# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_scheme', '0003_coursescheme_courses'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='coursescheme',
            unique_together=set([('batch', 'year', 'branch')]),
        ),
    ]
