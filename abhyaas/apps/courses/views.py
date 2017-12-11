from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.template.response import TemplateResponse
from .models import CurrentCourse,UploadMetadata
from django.contrib.auth.decorators import login_required,user_passes_test
from .forms import UploadFileForm
import dropbox
from utils.file_utils import check,list_files,get_download_link
# Create your views here.
access_token = 'oWw_iYHAydcAAAAAAAAA1UQIMnh-LpfBDd9mnqNlNcfTg5dCdepmD42C2htSajap'
dbx = dropbox.Dropbox(access_token)

@login_required(login_url="/login/login/")
def index(request):
	context = RequestContext(request)
	course_code = request.GET.get('code')
	ccourse = CurrentCourse.objects.get(course_code=course_code)
	files_metadata = UploadMetadata.objects.filter(course=ccourse)
	course_files = []
	for fm in files_metadata:
		dlink = get_download_link(dbx,course_code,fm.filename)
		course_files.append((fm,dlink))
	data = {'course_code':course_code,'course_files':course_files}
	return TemplateResponse(request,'courses/course_page.html',data)


@login_required(login_url="/login/login/")
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







