# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20171206_1002'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadMetadata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(max_length=50)),
                ('course', models.ForeignKey(to='courses.CurrentCourse')),
                ('uploader', models.ForeignKey(to='login.Faculty')),
            ],
        ),
    ]
