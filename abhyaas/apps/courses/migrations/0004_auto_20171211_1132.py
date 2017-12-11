# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20171206_1002'),
        ('courses', '0003_coursenotification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('name', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('deadline', models.DateField()),
                ('filename', models.CharField(max_length=255)),
                ('course', models.ForeignKey(to='courses.CurrentCourse')),
                ('uploader', models.ForeignKey(to='login.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentSubmission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('solution_file', models.CharField(max_length=255)),
                ('submit_date', models.DateField()),
                ('status', models.CharField(max_length=2, choices=[(b'NS', b'Not Submitted'), (b'S', b'Submitted'), (b'E', b'Evaluated')])),
                ('assignment', models.ForeignKey(to='courses.Assignment')),
                ('student', models.ForeignKey(to='login.Student')),
            ],
        ),
        migrations.AddField(
            model_name='uploadmetadata',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 11, 11, 32, 54, 261034)),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='assignmentsubmission',
            unique_together=set([('student', 'assignment')]),
        ),
    ]
