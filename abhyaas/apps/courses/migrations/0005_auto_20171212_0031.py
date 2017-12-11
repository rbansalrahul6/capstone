# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20171211_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assignment',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='assignment',
            unique_together=set([('course', 'name', 'filename')]),
        ),
        migrations.AlterUniqueTogether(
            name='uploadmetadata',
            unique_together=set([('course', 'filename')]),
        ),
    ]
