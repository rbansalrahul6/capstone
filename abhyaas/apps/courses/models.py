from django.db import models
from college.models import Branch
from login.models import Faculty
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

