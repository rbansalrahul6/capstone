from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from courses.models import CourseFacultyMap
from login.models import Faculty

# Create your views here.
@login_required(login_url="/login/login/")
def index(request):
	context = RequestContext(request)
	return render_to_response('faculty/faculty.html',{},context)


@login_required(login_url="/login/login/")
def get_profile(request):
	context = RequestContext(request)
	department=None
	if request.user.is_authenticated():
		uname = request.user.username
		faculty = Faculty.objects.get(username=uname)
		department=faculty.dept
	data = {"Dept":department}
	return render_to_response('faculty/profile.html',data,context)

@login_required(login_url="/login/login/")
def show_courses(request):
	context = RequestContext(request)
	courses= None
	if request.user.is_authenticated():
		uname = request.user.username
		fac = Faculty.objects.get(username=uname)
		courses = CourseFacultyMap.objects.filter(faculty=fac)
	data = {"list":courses}
	return render_to_response('faculty/mycourses.html',data,context)

