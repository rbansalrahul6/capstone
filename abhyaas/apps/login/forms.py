from django import forms
from django.contrib.auth.models import User
from login.models import UserProfile,MyUser
from students.models import Student


'''class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    user_type = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = MyUser
        #exclude=('user_type',)
        fields = ('username','email','password','first_name','last_name','user_type')

class StudentProfileForm(forms.ModelForm):
    branch = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Student
        fields = ('roll_no','branch')'''