# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20171206_1002'),
        ('college', '0002_auto_20171124_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseFacultyMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseStudentMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('batch', models.IntegerField(choices=[(2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017)])),
                ('branch', models.ForeignKey(to='college.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='CurrentCourse',
            fields=[
                ('course_code', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('course_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='coursestudentmap',
            name='course',
            field=models.ForeignKey(to='courses.CurrentCourse'),
        ),
        migrations.AddField(
            model_name='coursefacultymap',
            name='course',
            field=models.ForeignKey(to='courses.CurrentCourse'),
        ),
        migrations.AddField(
            model_name='coursefacultymap',
            name='faculty',
            field=models.ForeignKey(to='login.Faculty'),
        ),
        migrations.AlterUniqueTogether(
            name='coursestudentmap',
            unique_together=set([('batch', 'course', 'branch')]),
        ),
        migrations.AlterUniqueTogether(
            name='coursefacultymap',
            unique_together=set([('course', 'faculty')]),
        ),
    ]
