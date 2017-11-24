# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_scheme', '0005_auto_20171124_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursescheme',
            name='branch',
            field=models.ForeignKey(to='college.Branch', to_field=b'branch_name'),
        ),
    ]
