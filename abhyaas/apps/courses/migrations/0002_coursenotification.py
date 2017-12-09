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
            name='CourseNotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=90)),
                ('description', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(to='courses.CurrentCourse')),
                ('sender', models.ForeignKey(to='login.Faculty')),
            ],
        ),
    ]
