from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from django.http import HttpResponse
from courses.models import CourseFacultyMap,CourseStudentMap, CurrentCourse, CourseNotification
from login.models import Faculty,Student
from faculty.forms import NotificationForm
from notifications.signals import notify


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

@login_required(login_url="/login/login/")
def send_notification(request):
	context=RequestContext(request)
	if request.method == 'POST':
		notify_form=NotificationForm(request.POST,user=request.user)
		if notify_form.is_valid():
			#notify_form.save()
			msg= notify_form.cleaned_data['message']
			send_to= notify_form.cleaned_data['send_to']
			linkedcourse=CurrentCourse.objects.get(course_code=send_to)
			CourseNotification(course=linkedcourse,
				message=msg,sender=Faculty.objects.get(username
					=request.user.username),description="").save()
			
			linkedbatch=CourseStudentMap.objects.filter(course=linkedcourse)
			for b in linkedbatch:
				linkedstu=Student.objects.filter(batch=b.batch,branch=b.branch)
				notify.send(request.user, recipient=linkedstu, verb=msg)
			return HttpResponse("sent successfully")		
	else:
		notify_form=NotificationForm(user=request.user)
	return render_to_response(
		'faculty/sendnotification.html',
		{'notify_form':notify_form},
		context
		)


