from django.db import models
from college.models import Branch
from login.models import Faculty,Student
import datetime

# Create your models here.
class CurrentCourse(models.Model):
	course_code = models.CharField(max_length=10,primary_key=True)
	course_name = models.CharField(max_length=20)
	# list of departments or pick automatically from course code

	def __str__(self):
		return self.course_code

class CourseStudentMap(models.Model):
	course=models.ForeignKey(CurrentCourse,on_delete=models.CASCADE)
	branch=models.ForeignKey(Branch,on_delete=models.CASCADE)

	year_dropdown = []
	curr = datetime.datetime.now().year
	for y in range(curr-4,curr+1):
		year_dropdown.append((y,y))
	batch = models.IntegerField(choices=year_dropdown)
	class Meta:
		unique_together = ('batch','course','branch')


class CourseFacultyMap(models.Model):
	course=models.ForeignKey(CurrentCourse,on_delete=models.CASCADE)
	faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
	class Meta:
		unique_together = ('course','faculty')

class UploadMetadata(models.Model):
	course=models.ForeignKey(CurrentCourse,on_delete=models.CASCADE)
	filename=models.CharField(max_length=50)
	uploader=models.ForeignKey(Faculty,on_delete=models.CASCADE)
	upload_time = models.DateTimeField()

	class Meta:
		unique_together = ('course','filename')	

class CourseNotification(models.Model):
 	course=models.ForeignKey(CurrentCourse,on_delete=models.CASCADE)
 	message=models.CharField(max_length=90)
 	description=models.TextField()
 	time=models.DateTimeField(auto_now_add=True)
 	sender=models.ForeignKey(Faculty)

class Assignment(models.Model):
	name = models.CharField(max_length=255)
	course = models.ForeignKey(CurrentCourse,on_delete=models.CASCADE)
	uploader = models.ForeignKey(Faculty,on_delete=models.CASCADE)
	deadline = models.DateField()
	filename = models.CharField(max_length=255)
	instructions = models.TextField()
	max_marks = models.PositiveIntegerField(default=0)
	class Meta:
			unique_together = ('course','name','filename')
	def __str__(self):
		return self.name	

class AssignmentSubmission(models.Model):
	assignment = models.ForeignKey(Assignment)
	student = models.ForeignKey(Student,on_delete=models.CASCADE)
	solution_file = models.CharField(max_length=255)
	submit_date = models.DateField()
	STATUS_CHOICES = (
		('S','Submitted'),
		('E','Evaluated'),
		)
	status = models.CharField(max_length=2,choices=STATUS_CHOICES)
	marks = models.PositiveIntegerField(default=0)
	class Meta:
		unique_together = ('student','assignment')	



