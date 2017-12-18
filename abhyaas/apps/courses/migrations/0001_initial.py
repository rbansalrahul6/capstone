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
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('deadline', models.DateField()),
                ('filename', models.CharField(max_length=255)),
                ('instructions', models.TextField(null=True)),
                ('max_marks', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='AssignmentSubmission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('solution_file', models.CharField(max_length=255)),
                ('submit_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(max_length=2, choices=[(b'S', b'Submitted'), (b'E', b'Evaluated')])),
                ('marks', models.PositiveIntegerField(default=0)),
                ('remarks', models.TextField(null=True, blank=True)),
                ('assignment', models.ForeignKey(to='courses.Assignment')),
                ('student', models.ForeignKey(to='login.Student')),
            ],
        ),
        migrations.CreateModel(
            name='CourseFacultyMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseNotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=90)),
                ('description', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
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
        migrations.CreateModel(
            name='UploadMetadata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(max_length=50)),
                ('upload_date', models.DateField(auto_now_add=True)),
                ('course', models.ForeignKey(to='courses.CurrentCourse')),
                ('uploader', models.ForeignKey(to='login.Faculty')),
            ],
        ),
        migrations.AddField(
            model_name='coursestudentmap',
            name='course',
            field=models.ForeignKey(to='courses.CurrentCourse'),
        ),
        migrations.AddField(
            model_name='coursenotification',
            name='course',
            field=models.ForeignKey(to='courses.CurrentCourse'),
        ),
        migrations.AddField(
            model_name='coursenotification',
            name='sender',
            field=models.ForeignKey(to='login.Faculty'),
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
        migrations.AddField(
            model_name='assignment',
            name='course',
            field=models.ForeignKey(to='courses.CurrentCourse'),
        ),
        migrations.AddField(
            model_name='assignment',
            name='uploader',
            field=models.ForeignKey(to='login.Faculty'),
        ),
        migrations.AlterUniqueTogether(
            name='uploadmetadata',
            unique_together=set([('course', 'filename')]),
        ),
        migrations.AlterUniqueTogether(
            name='coursestudentmap',
            unique_together=set([('batch', 'course', 'branch')]),
        ),
        migrations.AlterUniqueTogether(
            name='coursefacultymap',
            unique_together=set([('course', 'faculty')]),
        ),
        migrations.AlterUniqueTogether(
            name='assignmentsubmission',
            unique_together=set([('student', 'assignment')]),
        ),
        migrations.AlterUniqueTogether(
            name='assignment',
            unique_together=set([('course', 'name', 'filename')]),
        ),
    ]
