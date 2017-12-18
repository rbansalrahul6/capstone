from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from courses.models import CourseStudentMap,CurrentCourse,CourseNotification,Assignment,AssignmentSubmission
from login.models import Student
from django.http import HttpResponse
from courses import views as course_views
from django.http import HttpResponse
from django.conf import settings
import os
import dropbox
import datetime
from utils.file_utils import upload_to_dropbox,check,create_folder,get_download_link,student_check,is_notadmin

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
@user_passes_test(student_check,login_url=settings.LOGIN_URL)
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
@user_passes_test(student_check,login_url=settings.LOGIN_URL)
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
@user_passes_test(student_check,login_url=settings.LOGIN_URL)
def show_courses(request):
	context = RequestContext(request)
	course_view = course_views.show_courses(request,Student,CourseStudentMap)
	course_view.render()
	user=Student.objects.get(username=request.user.username)
	data=course_view.context_data
	data['unread_no']=len(user.notifications.unread())
	return render_to_response('students/mycourses.html',data,context)

@login_required(login_url="/login/login/")
@user_passes_test(student_check,login_url=settings.LOGIN_URL)
def course_page(request):
	context = RequestContext(request)
	course_page_view = course_views.index(request)
	course_page_view.render()
	return render_to_response('students/course_page.html',course_page_view.context_data,context)

@login_required(login_url="/login/login/")
@user_passes_test(student_check,login_url=settings.LOGIN_URL)
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
@user_passes_test(student_check,login_url=settings.LOGIN_URL)
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

@login_required(login_url="/login/login/")
@user_passes_test(student_check,login_url=settings.LOGIN_URL)	
def show_assignments(request):
	course_code = request.GET.get('code')
	ccourse = CurrentCourse.objects.get(course_code=course_code)
	student = Student.objects.get(username=request.user.username)
	assignments_list = Assignment.objects.filter(course=ccourse)
	not_submitted = []
	submitted = []
	for a in assignments_list:
		alink = get_download_link(dbx,course_code,a.filename,'assignments')
		try:
			asub = AssignmentSubmission.objects.get(student=student,assignment=a)
			sfilename = student.username + '|' + asub.solution_file
			slink = get_download_link(dbx,course_code,sfilename,'submissions')
			submitted.append((asub,alink,slink))
		except AssignmentSubmission.DoesNotExist:
			asub = None
			not_submitted.append((a,alink))
	data = {'course_code':course_code,'submitted':submitted,'unsubmitted':not_submitted}
	return render(request,'students/course_assignments.html',data)

#dropbox data
access_token = 'oWw_iYHAydcAAAAAAAAA1UQIMnh-LpfBDd9mnqNlNcfTg5dCdepmD42C2htSajap'
dbx = dropbox.Dropbox(access_token)

@login_required(login_url="/login/login/")
@user_passes_test(student_check,login_url=settings.LOGIN_URL)
def submit_assignment(request):
	course_code = request.GET.get('code')
	aname = request.GET.get('aname')
	ccourse = CurrentCourse.objects.get(course_code=course_code)
	assignment = Assignment.objects.get(course=ccourse,name=aname)
	student = Student.objects.get(username=request.user.username)
	alink = get_download_link(dbx,course_code,assignment.filename,'assignments')
	sfile = None
	if request.method=='POST' and request.FILES['sfile']:
		sfile = request.FILES['sfile']
	if sfile is not None:
		sub_folder = os.path.join(course_code,'submissions')
		if not check(dbx,sub_folder):
			create_folder(dbx,sub_folder)
		filename = student.username + '|' + sfile.name
		result = upload_to_dropbox(dbx,sfile,filename,course_code,datetime.datetime.now(),subfolder='submissions')
		asub = AssignmentSubmission(assignment=assignment,student=student,solution_file=sfile.name,
			status='S')
		asub.save()
		print result
	data = {'assgn':assignment,'course_code':course_code,'alink':alink}
	return render(request,'students/submit_assignment.html',data)		
