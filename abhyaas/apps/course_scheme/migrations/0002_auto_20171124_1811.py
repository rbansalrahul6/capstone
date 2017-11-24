# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_scheme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursescheme',
            name='semester',
            field=models.IntegerField(default=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='courseitem',
            name='remarks',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='coursescheme',
            name='batch',
            field=models.IntegerField(choices=[(2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017)]),
        ),
        migrations.AlterUniqueTogether(
            name='coursescheme',
            unique_together=set([('batch', 'semester', 'branch')]),
        ),
        migrations.RemoveField(
            model_name='coursescheme',
            name='year',
        ),
    ]
