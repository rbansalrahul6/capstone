# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_auto_20171124_1705'),
        ('course_scheme', '0011_auto_20171207_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subgroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('batch', models.IntegerField(choices=[(2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017)])),
                ('no_of_subgroups', models.PositiveIntegerField(default=0)),
                ('branch', models.ForeignKey(to='college.Branch')),
            ],
        ),
    ]
