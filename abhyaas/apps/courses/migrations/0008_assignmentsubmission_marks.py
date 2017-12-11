# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20171212_0328'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignmentsubmission',
            name='marks',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
