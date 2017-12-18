from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.template.response import TemplateResponse
from login.models import Student,Faculty
from .models import CurrentCourse,UploadMetadata,CourseNotification
from django.contrib.auth.decorators import login_required,user_passes_test
from .forms import UploadFileForm
from django.conf import settings
import dropbox
from utils.file_utils import check,get_download_link,is_notadmin
# Create your views here.
access_token = 'oWw_iYHAydcAAAAAAAAA1UQIMnh-LpfBDd9mnqNlNcfTg5dCdepmD42C2htSajap'
dbx = dropbox.Dropbox(access_token)

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

@login_required(login_url="/login/login/")
@user_passes_test(is_notadmin,login_url='/login/login/')
def index(request):
	context = RequestContext(request)
	course_code = request.GET.get('code')
	ccourse = CurrentCourse.objects.get(course_code=course_code)
	files_metadata = UploadMetadata.objects.filter(course=ccourse)
	course_files = []
	for fm in files_metadata:
		dlink = get_download_link(dbx,course_code,fm.filename)
		course_files.append((fm,dlink))
	data = {'course_code':course_code,'course_files':course_files,'course_name':ccourse.course_name}
	return TemplateResponse(request,'courses/course_page.html',data)

@login_required(login_url="/login/login/")
@user_passes_test(is_notadmin,login_url='/login/login/')
def show_courses(request,user_model,course_map):
	context = RequestContext(request)
	courses = None
	user = request.user
	uname = user.username
	if user.utype=='F':
		faculty = user_model.objects.get(username=uname)
		courses = course_map.objects.filter(faculty=faculty)
	elif user.utype=='S':
		student = user_model.objects.get(username=uname)
		courses = course_map.objects.filter(branch=student.branch,batch=student.batch)
	data = {"list":courses}
	return TemplateResponse(request,'courses/list_courses.html',data)

@login_required(login_url="/login/login/")
@user_passes_test(is_notadmin,login_url='/login/login/')
def view_announcement(request):
	context=RequestContext(request)
	course_code = request.GET.get('code')
	ccourse=CurrentCourse.objects.get(course_code=course_code)
	announcement=CourseNotification.objects.get(id=request.GET.get('id'))
	#unreadlist_course,unreadlist_desc=getdesc_coursecode(user.notifications.unread().values_list('description',flat=True))
	data={"announcement":announcement,"course_code":course_code,"course_name":ccourse.course_name}
	if request.user.utype=='F':
		return render_to_response('faculty/viewannounce_page.html',data,context)
	else:
		return render_to_response('students/viewannounce_page.html',data,context)		

@login_required(login_url="/login/login/")
@user_passes_test(is_notadmin,login_url='/login/login/')
def view_message(request):
	context=RequestContext(request)
	if request.user.utype=='S':
		user=Student.objects.get(username=request.user.username)
	else:
		user=Faculty.objects.get(username=request.user.username)

	mid=int(request.GET.get('id'))
	print mid
	readlist_course,readlist_desc=getdesc_coursecode(user.notifications.read()
		.values_list('description',flat=True))
	readlist_otherfields=user.notifications.read()
	read_no=len(readlist_otherfields)
	read_zip=zip(readlist_course,readlist_desc,readlist_otherfields)
	senditem=None
	for item in read_zip:
		print item[2].id,type(item[2].id),type(mid)
		if item[2].id==mid:
			senditem=item
			break


	print senditem
	# print type(unreadlist_course),type(unreadlist_desc),type(unreadlist_otherfields),type(unread_zip)
	# return render_to_response('courses/inbox.html',{"unread_zip":unread_zip},context
	# data={"announcement":announcement,"course_code":course_code,"course_name":ccourse.course_name}
	if request.user.utype=='S':
		return render_to_response('students/viewmessage_page.html',{"announcement":senditem},context)
	else:
	 	return render_to_response('faculty/viewmessage_page.html',{"announcement":senditem},context)





