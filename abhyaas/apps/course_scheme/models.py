from django.db import models
import datetime
# Create your models here.

class Course(models.Model):
	course_code = models.CharField(max_length=10,primary_key=True)
	course_name = models.CharField(max_length=20)
	# list of departments

	def __str__(self):
		return self.course_code

class CourseScheme(models.Model):
	# year_dropdown = []
	# curr = datetime.datetime.now().year
	# for y in range(curr-5,curr):
	# 	year_dropdown.append((y,y))
	SAMPLE_BATCH_CHOICES = (
		('2014','2014'),
		('2015','2015'),
		('2016','2016'),
		('2017','2017'),
		)
	batch = models.CharField(max_length=5,choices=SAMPLE_BATCH_CHOICES)
	YEAR_CHOICES = (
		('1','1st'),
		('2','2nd'),
		('3','3rd'),
		('4','4th'),
		)
	year = models.CharField(max_length=1,choices=YEAR_CHOICES)
	SAMPLE_BRANCH_CHOICES = (
		('COE','Computer Science'),
		('ECE','Electronics & Communications'),
		('CIE','Civil Engineering'),
		)
	branch = models.CharField(max_length=5,choices=SAMPLE_BRANCH_CHOICES)
	# test
	courses = models.ManyToManyField(Course)
	class Meta:
		unique_together = ('batch','year','branch')
	def __str__(self):
		return "%s-%s-%s" % (self.batch,self.year,self.branch)