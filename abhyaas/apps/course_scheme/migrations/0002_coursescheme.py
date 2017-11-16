# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_scheme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseScheme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('batch', models.CharField(default=2017, max_length=4, choices=[(2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016)])),
                ('year', models.CharField(max_length=1, choices=[(b'1', b'1st'), (b'2', b'2nd'), (b'3', b'3rd'), (b'4', b'4th')])),
                ('branch', models.CharField(max_length=5, choices=[(b'COE', b'Computer Science'), (b'ECE', b'Electronics & Communications'), (b'CIE', b'Civil Engineering')])),
            ],
        ),
    ]
