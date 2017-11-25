# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='dept',
            field=models.ForeignKey(to='college.Department'),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.ForeignKey(to='college.Branch'),
        ),
    ]
