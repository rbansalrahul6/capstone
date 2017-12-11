from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from courses.models import CourseFacultyMap
from login.models import Faculty
from faculty.forms import UploadFileForm
from courses import views as course_views
from courses.models import CurrentCourse,UploadMetadata
import os
import datetime
import dropbox
from utils.file_utils import upload_to_dropbox,check,create_folder
# Create your views here.
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

