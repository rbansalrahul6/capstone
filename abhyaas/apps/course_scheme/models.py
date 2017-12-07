from django.db import models
from college.models import Branch
from login.models import Faculty
import datetime
# Create your models here.
class Course(models.Model):
	course_code = models.CharField(max_length=10,primary_key=True)
	course_name = models.CharField(max_length=50)
	# list of departments or pick automatically from course code
	
	def __str__(self):
		return self.course_code

# like painter
class CourseScheme(models.Model):
	year_dropdown = []
	curr = datetime.datetime.now().year
	for y in range(curr-4,curr+1):
		year_dropdown.append((y,y))
	
	batch = models.IntegerField(choices=year_dropdown)
	sem_list = range(1,9)
	SEMESTER_CHOICES = tuple(zip(sem_list,sem_list))
	semester = models.IntegerField(choices=SEMESTER_CHOICES,default=1)
	branch = models.ForeignKey(Branch)
	

	class Meta:
		unique_together = ('batch','semester','branch')
	def __str__(self):
		return "%s-%s-%s" % (self.batch,self.semester,self.branch)  


# like picture
class CourseItem(models.Model):
	COURSE_TYPES = (('R','Regular'),('E','Elective'))
	course = models.ForeignKey(Course,on_delete=models.CASCADE)
	course_type = models.CharField(max_length=1,choices=COURSE_TYPES,default='R')
	remarks = models.CharField(max_length=255,null=True,blank=True)
	course_scheme = models.ForeignKey(CourseScheme,on_delete=models.CASCADE)
	is_current=models.BooleanField(default=False)


####### FOR TESTING OF FACULTY MAPPING #########

# like review

class FacultyMapping(models.Model):
	faculty = models.ForeignKey(Faculty)
	course_item = models.ForeignKey(CourseItem,on_delete=models.CASCADE) # no cascade maybe

	def __str__(self):
		return self.faculty.first_name                                                       