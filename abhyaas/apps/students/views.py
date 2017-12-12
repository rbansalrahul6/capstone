from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from courses.models import CourseStudentMap,CurrentCourse,CourseNotification
from login.models import Student
from courses import views as course_views
from django.http import HttpResponse

def getdesc_coursecode(notif):
	list2=[]
 	for i in notif:
 		list2.append(i.encode('utf8'))
 	list3=[]
 	list_course=[]	
 	for i in list2:
 		try:
 			(m,n)=i.split('_',1)

 			list3.append(n)
 			list_course.append(m+" "+CurrentCourse.objects.get(course_code=m).course_name)
 		except:
 			list3.append(i)
 	return list_course,list3	
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
def show_inbox(request):
	context=RequestContext(request)
	user=Student.objects.get(username=request.user.username)
	unreadlist_course,unreadlist_desc=getdesc_coursecode(user.notifications.unread()
		.values_list('description',flat=True))
	unreadlist_otherfields=user.notifications.unread()
	unread_no=len(unreadlist_otherfields)
	readlist_course,readlist_desc=getdesc_coursecode(user.notifications.read()
		.values_list('description',flat=True))
	readlist_otherfields=user.notifications.read()
	read_no=len(readlist_otherfields)
	unread_zip=zip(unreadlist_course,unreadlist_desc,unreadlist_otherfields)
	read_zip=zip(readlist_course,readlist_desc,readlist_otherfields)
	user.notifications.mark_all_as_read()
	print unreadlist_course,unreadlist_desc,unreadlist_otherfields,unread_zip
	print type(unreadlist_course),type(unreadlist_desc),type(unreadlist_otherfields),type(unread_zip)
	return render_to_response('students/inbox.html',{"unread_zip":unread_zip,"read_zip":read_zip},context)

@login_required(login_url="/login/login/")
def show_announcement(request):
	context=RequestContext(request)
	course_code = request.GET.get('code')
	
	user=Student.objects.get(username=request.user.username)
	
	course=CurrentCourse.objects.get(course_code=course_code)
	notif=CourseNotification.objects.filter(course=course)
	ccourse=CurrentCourse.objects.get(course_code=course_code)
	#unreadlist_course,unreadlist_desc=getdesc_coursecode(user.notifications.unread().values_list('description',flat=True))
	data={"notif":notif,"course_code":course_code,"course_name":ccourse.course_name}
	return render_to_response('students/announcement_page.html',data,context)	
