# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_assignment_max_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentsubmission',
            name='remarks',
            field=models.TextField(null=True, blank=True),
        ),
    ]
