# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20171124_1855'),
        ('course_scheme', '0007_auto_20171124_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyMapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_item', models.ForeignKey(to='course_scheme.CourseItem')),
            ],
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='course_item',
        ),
        migrations.DeleteModel(
            name='Faculty',
        ),
        migrations.AddField(
            model_name='facultymapping',
            name='faculty',
            field=models.ForeignKey(to='login.Faculty'),
        ),
    ]
