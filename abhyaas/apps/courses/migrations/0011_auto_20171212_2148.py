# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_assignmentsubmission_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentsubmission',
            name='submit_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
