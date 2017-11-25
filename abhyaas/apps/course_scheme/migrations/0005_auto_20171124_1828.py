# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_scheme', '0004_auto_20171124_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursescheme',
            name='branch',
            field=models.ForeignKey(to='college.Branch'),
        ),
    ]
