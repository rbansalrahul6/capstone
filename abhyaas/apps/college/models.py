from django.db import models

# Create your models here.
class Branch(models.Model):
	branch_name = models.CharField(max_length=255,unique=True)
	branch_code = models.CharField(max_length=255,primary_key=True)

	class Meta:
		verbose_name_plural = 'Branches'

	def __str__(self):
		return self.branch_code

class Department(models.Model):
	department_name = models.CharField(max_length=255,primary_key=True)
	short_name = models.CharField(max_length=255,null=True,blank=True)

	def __str__(self):
		return self.department_name