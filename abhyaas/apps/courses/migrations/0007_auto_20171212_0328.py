# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_assignment_instructions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentsubmission',
            name='status',
            field=models.CharField(max_length=2, choices=[(b'S', b'Submitted'), (b'E', b'Evaluated')]),
        ),
    ]
