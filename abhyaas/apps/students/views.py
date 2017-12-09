from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from courses.models import CourseStudentMap
from login.models import Student

# Create your views here.
@login_required(login_url="/login/login/")
def index(request):
	context = RequestContext(request)
	return render_to_response('students/student.html',{},context)


@login_required(login_url="/login/login/")
def get_profile(request):
	context = RequestContext(request)
	branch = None
	if request.user.is_authenticated():
		uname = request.user.username
		student = Student.objects.get(username=uname)
		branch = student.branch
	data = {"Branch":branch}
	return render_to_response('students/profile.html',data,context)

@login_required(login_url="/login/login/")
def show_courses(request):
	context = RequestContext(request)
	courses= None
	if request.user.is_authenticated():
		uname = request.user.username
		student = Student.objects.get(username=uname)
		courses = CourseStudentMap.objects.filter(branch=student.branch,batch=student.batch)
	data = {"list":courses}
	return render_to_response('students/mycourses.html',data,context)

@login_required(login_url="/login/login/")
def show_notifications(request):
	context = RequestContext(request)
	notif= None
	if request.user.is_authenticated():
		user=Student.objects.get(username=request.user.username)
		notif=user.notifications.unread()
		notif2=user.notifications.read()
		user.notifications.mark_all_as_read(user)
	data = {"unreadlist":notif,"readlist":notif2}
	return render_to_response('students/mynotifications.html',data,context)	

