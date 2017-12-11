from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from django.http import HttpResponse
from courses.models import CourseFacultyMap
from login.models import Faculty
from faculty.forms import UploadFileForm
from courses.models import CurrentCourse,CourseNotification,CourseFacultyMap,CourseStudentMap,UploadMetadata
from courses import views as course_views
from login.models import Student,Faculty
from notifications.signals import notify
import datetime
import os
import dropbox
from utils.file_utils import upload_to_dropbox,check,create_folder
# Create your views here.

# def getdesc_coursecode(notif):
# 	list2=[]
#  	for i in notif:
#  		list2.append(i.encode('utf8'))
#  	list3=[]
#  	list_course=[]	
#  	for i in list2:
#  		try:
#  			(m,n)=i.split('_',1)

#  			list3.append(n)
#  			list_course.append(m)
#  		except:
#  			list3.append(i)
#  	return list_course,list3		

 		


@login_required(login_url="/login/login/")
def index(request):
	context = RequestContext(request)
	# courses= None
	# if request.user.is_authenticated():
	# 	uname = request.user.username
	# 	fac = Faculty.objects.get(username=uname)
	# 	courses = CourseFacultyMap.objects.filter(faculty=fac)
	# data = {"list":courses}
	return render_to_response('faculty/sidebar.html',{},context)


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
def course_page(request):
	context = RequestContext(request)
	course_page_view = course_views.index(request)
	course_page_view.render()
	data=course_page_view.context_data
	return render_to_response('faculty/course_details.html',data,context)

@login_required(login_url="/login/login/")
def show_courses(request):
	context = RequestContext(request)
	course_view = course_views.show_courses(request,Faculty,CourseFacultyMap)
	course_view.render()
	data = course_view.context_data
	data['unread_no']=len(request.user.notifications.unread())
	return render_to_response('faculty/mycourses.html',data,context)

#dropbox data
access_token = 'oWw_iYHAydcAAAAAAAAA1UQIMnh-LpfBDd9mnqNlNcfTg5dCdepmD42C2htSajap'
dbx = dropbox.Dropbox(access_token)

@login_required(login_url="/login/login/")
def upload(request):
	myfile = None
	if request.method=='POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		filename = myfile.name
		print filename
	course_code = request.GET.get('code')
	ccourse = CurrentCourse.objects.get(course_code=course_code)
	faculty = Faculty.objects.get(username=request.user.username)
	if myfile is not None:
		if not check(dbx,course_code):
			create_folder(dbx,course_code)
		curr_time = datetime.datetime.now()
		result = upload_to_dropbox(dbx,myfile,course_code,curr_time)
		metadata = UploadMetadata(uploader=faculty,course=ccourse,
			filename=myfile.name,upload_time=curr_time)
		metadata.save()
		print result
	return render(request,'faculty/upload.html')

@login_required(login_url="/login/login/")
def show_announcement(request):
	context=RequestContext(request)
	course_code = request.GET.get('code')
	
	user=Faculty.objects.get(username=request.user.username)
	
	course=CurrentCourse.objects.get(course_code=course_code)
	notif=CourseNotification.objects.filter(course=course)
	#unreadlist_course,unreadlist_desc=getdesc_coursecode(user.notifications.unread().values_list('description',flat=True))
	data={"notif":notif,"course_code":course_code}
	return render_to_response('faculty/announcement_page.html',data,context)	

@login_required(login_url="/login/login/")
def send_announcement(request):
	context=RequestContext(request)
	if request.method == 'POST':
			print "here"
			subj= request.POST['subject']
			msg= request.POST['message']
			send_to= request.POST['course_code']
			linkedcourse=CurrentCourse.objects.get(course_code=send_to)
			CourseNotification(course=linkedcourse,
				message=msg,sender=Faculty.objects.get(username
					=request.user.username),description=msg).save()
			
			linkedbatch=CourseStudentMap.objects.filter(course=linkedcourse)
			for b in linkedbatch:
				linkedstu=Student.objects.filter(batch=b.batch,branch=b.branch)
				notify.send(request.user, recipient=linkedstu, verb=subj, description=msg)
			linkedfac=CourseFacultyMap.objects.filter(course=linkedcourse)
			for fac in linkedfac:
				notify.send(request.user, recipient=Faculty.objects.get(username=fac.faculty.username), verb=subj, description=send_to+"_"+msg)	
			return HttpResponse("sent successfully")		
	else:
		course_code = request.GET.get('code')
		# To get course from description
		# user=Faculty.objects.get(username=request.user.username)
 	# 	notif=user.notifications.unread().values_list('description',flat=True)
 	# 	list2=[]
 	# 	for i in notif:
 	# 		list2.append(i.encode('utf8'))
 	# 	list3=[]
 	# 	list_course=[]	
 	# 	for i in list2:
 	# 		try:
 	# 			(m,n)=i.split('_',1)

 	# 			list3.append(n)
 	# 			list_course.append(m)
 	# 		except:
 	# 			list3.append(i)	
 	# 	print list_course
 		ccourse=CurrentCourse.objects.get(course_code=course_code)
		return render_to_response('faculty/newannounce.html',{"course_code":course_code},context)	

