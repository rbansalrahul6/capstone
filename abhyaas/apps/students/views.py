from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from courses.models import CourseStudentMap
from login.models import Student
from courses import views as course_views
from courses.models import CurrentCourse,Assignment,AssignmentSubmission
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

def show_assignments(request):
	course_code = request.GET.get('code')
	ccourse = CurrentCourse.objects.get(course_code=course_code)
	student = Student.objects.get(username=request.user.username)
	assignments_list = Assignment.objects.filter(course=ccourse)
	not_submitted = []
	submitted = []
	for a in assignments_list:
		try:
			asub = AssignmentSubmission.objects.get(student=student,assignment=a)
			submitted.append(asub)
		except AssignmentSubmission.DoesNotExist:
			asub = None
			not_submitted.append(a)
	data = {'course_code':course_code,'submitted':submitted,'unsubmitted':not_submitted}
	return render(request,'students/course_assignments.html',data)

def submit_assignment(request):
	course_code = request.GET.get('code')
	aname = request.GET.get('aname')
	ccourse = CurrentCourse.objects.get(course_code=course_code)
	assignment = Assignment.objects.get(course=ccourse,name=aname)
	student = Student.objects.get(username=request.user.username)
	data = {'assgn':assignment,'course_code':course_code}
	return render(request,'students/submit_assignment.html',data)

