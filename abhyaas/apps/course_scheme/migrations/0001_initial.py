# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_code', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('course_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CourseItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_type', models.CharField(default=b'R', max_length=1, choices=[(b'R', b'Regular'), (b'E', b'Elective')])),
                ('remarks', models.CharField(max_length=255)),
                ('course', models.ForeignKey(to='course_scheme.Course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseScheme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('batch', models.CharField(max_length=5, choices=[(b'2014', b'2014'), (b'2015', b'2015'), (b'2016', b'2016'), (b'2017', b'2017')])),
                ('year', models.CharField(max_length=1, choices=[(b'1', b'1st'), (b'2', b'2nd'), (b'3', b'3rd'), (b'4', b'4th')])),
                ('branch', models.CharField(max_length=5, choices=[(b'COE', b'Computer Science'), (b'ECE', b'Electronics & Communications'), (b'CIE', b'Civil Engineering')])),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('short_name', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('course_item', models.ForeignKey(to='course_scheme.CourseItem')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='coursescheme',
            unique_together=set([('batch', 'year', 'branch')]),
        ),
        migrations.AddField(
            model_name='courseitem',
            name='course_scheme',
            field=models.ForeignKey(to='course_scheme.CourseScheme'),
        ),
    ]
