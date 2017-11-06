from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from login.models import *
# Register your models here.

class UserForm(forms.ModelForm):
	class Meta:
		model = BaseUser
		exclude = ('groups','user_permissions','is_staff','is_active','is_superuser','last_login','date_joined')

class UCExtended(UserCreationForm):
	def __init__(self,*args,**kwargs):
		super(UCExtended,self).__init__(*args,**kwargs)
		self.fields['email'] = forms.EmailField(label='Email',max_length=75)
		self.fields['email'].label='myEmail'

class BaseUserAdmin(UserAdmin):
	#fields = ('email',)
	#form = UserForm
	#add_form = UCExtended
	'''fieldsets = (
		(None,{'fields':('email','name','utype')}),
		(None,{'fields':()})
		)'''
	add_fieldsets = (
		(None,{'classes':('wide',),'fields':('email','username','password1','password2')}
			),
		)
	#exclude = ('groups','user_permissions','is_staff','is_active','is_superuser','last_login','date_joined')
	list_display = ('username','password','utype')

class CommonAdmin(UserAdmin):
	add_fieldsets = (
		(None,{'classes':('wide',),'fields':('first_name','last_name')}
			),
		)
	#pass
	#fields = ('branch','sem')
	'''fieldsets = (
		(None,{'fields':('branch','sem')}),
		(None,{'fields':()})
		)'''
	#exclude = ('groups','user_permissions','is_staff','is_active','is_superuser','last_login','date_joined')



class StudentForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(StudentForm,self).__init__(*args,**kwargs)
		self.fields['username'].help_text='enter roll no'
		self.fields['username'].label='Roll No'


class FacultyForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		super(FacultyForm,self).__init__(*args,**kwargs)
		self.fields['username'].help_text='enter faculty id'
		self.fields['username'].label='Faculty Id'


class SimpleStudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = []
		#exclude = ('groups','user_permissions','is_staff','is_active','is_superuser','last_login','date_joined')
		labels = {'username':"Enrollment No",}
		help_texts = {'username':"Fill roll no",}

class SampleForm(UserChangeForm):
	class Meta(UserChangeForm.Meta):
		model = Student




class StudentAdmin(CommonAdmin):
	#form = SampleForm
	#fields = ('first_name','last_name','username','password','email','branch','sem','utype')
	'''fieldsets = (
		(None,{'fields':('branch','sem','utype')}),
		(None,{'fields':()})
		)'''
	add_fieldsets = CommonAdmin.add_fieldsets + (
		(None,{'classes':('wide',),'fields':('branch','username','password1','password2')}
			),
		)
	fieldsets =  (
            (None, {'fields': ('branch',)}),
    )
	#form = SimpleStudentForm


class FacultyAdmin(CommonAdmin):
	#fields = ('first_name','last_name','username','password','email','dept','desgn','utype')
	add_fieldsets = CommonAdmin.add_fieldsets + (
		(None,{'classes':('wide',),'fields':('dept','username','password1','password2')}
			),
		)
	fieldsets =  (
            (None, {'fields': ('dept',)}),
    )
	#form = FacultyForm



admin.site.register(BaseUser,BaseUserAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Faculty,FacultyAdmin)