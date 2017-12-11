from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from courses.models import CourseStudentMap,CurrentCourse,CourseNotification
from login.models import Student
from courses import views as course_views

# Create your views here.
@login_required(login_url="/login/login/")
def index(request):
	context = RequestContext(request)
	# courses= None
	# if request.user.is_authenticated():
	# 	uname = request.user.username
	# 	student = Student.objects.get(username=uname)
	# 	courses = CourseStudentMap.objects.filter(branch=student.branch,batch=student.batch)
	# data = {"list":courses}
	return render_to_response('students/sidebar.html',{},context)
	#return render_to_response('students/student.html',{},context)


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
	course_view = course_views.show_courses(request,Student,CourseStudentMap)
	course_view.render()
	user=Student.objects.get(username=request.user.username)
	data=course_view.context_data
	data['unread_no']=len(user.notifications.unread())
	return render_to_response('students/mycourses.html',data,context)

@login_required(login_url="/login/login/")
def course_page(request):
	context = RequestContext(request)
	course_page_view = course_views.index(request)
	course_page_view.render()
	return render_to_response('students/course_page.html',course_page_view.context_data,context)

@login_required(login_url="/login/login/")
def show_announcement(request):
	context=RequestContext(request)
	course_code = request.GET.get('code')
	
	user=Student.objects.get(username=request.user.username)
	
	course=CurrentCourse.objects.get(course_code=course_code)
	notif=CourseNotification.objects.filter(course=course)
	#unreadlist_course,unreadlist_desc=getdesc_coursecode(user.notifications.unread().values_list('description',flat=True))
	data={"notif":notif,"course_code":course_code}
	return render_to_response('students/announcement_page.html',data,context)	
