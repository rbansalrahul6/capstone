from django.db import models
from django.contrib.auth.models import AbstractUser
from college.models import Branch,Department
# Create your models here.

class BaseUser(AbstractUser):
	# all common fields
	USER_CHOICES = (('S','student'),('F','faculty'))
	utype = models.CharField(max_length=1,choices=USER_CHOICES)
	name = models.CharField(max_length=50)
	

class Student(BaseUser):
	#roll_no = models.CharField(max_length=10,db_column='username')
	#BaseUser._meta.get_field('username').verbose_name='Roll No'
	'''def __init__(self, *args, **kwargs):
		super(BaseUser,self).__init__(*args, **kwargs)
		self._meta.get_field('username').verbose_name = 'Roll'''
	def __init__(self,*args,**kwargs):
		super(Student,self).__init__(*args,**kwargs)
		self.utype = 'S'
	def roll_no(self,obj):
		return ("%s" % self.username)
	roll_no.short_description = 'RollNo'
	branch = models.ForeignKey(Branch)
	sem = models.CharField(max_length=10,blank=True)
	#self.username.verbose_name='RollNo'

	class Meta:
		verbose_name='Student'

class Faculty(BaseUser):
	#BaseUser._meta.get_field('username').verbose_name='fid'
	def __init__(self,*args,**kwargs):
		super(Faculty,self).__init__(*args,**kwargs)
		self.utype = 'F'
	dept = models.ForeignKey(Department)
	desgn = models.CharField(max_length=20)

	class Meta:
		verbose_name='Faculty'
		verbose_name_plural='Faculties'



