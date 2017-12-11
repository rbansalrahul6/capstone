# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_assignmentsubmission_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='max_marks',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
