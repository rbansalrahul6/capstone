# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_scheme', '0002_coursescheme'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursescheme',
            name='courses',
            field=models.ManyToManyField(to='course_scheme.Course'),
        ),
    ]
