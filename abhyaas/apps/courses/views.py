from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required,user_passes_test
import dropbox
from utils.file_utils import check,list_files,download
import utils.constants as constants
import os
# Create your views here.
access_token = 'oWw_iYHAydcAAAAAAAAA1UQIMnh-LpfBDd9mnqNlNcfTg5dCdepmD42C2htSajap'
dbx = dropbox.Dropbox(access_token)

def index(request):
	context = RequestContext(request)
	course_code = request.GET.get('code')
	course_files = None
	if check(dbx,course_code):
		course_files = list_files(dbx,course_code)
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

def download_file(request):
	course_code = request.GET.get('code')
	filename = request.GET.get('file')
	file_data = download(dbx,course_code,filename)
	download_dir = constants.DOWNLOAD_DIR
	course_dir = os.path.join(download_dir,course_code)
	if not os.path.exists(course_dir):
		os.makedirs(course_dir)
	with open(os.path.join(course_dir,filename),'wb') as f:
		f.write(file_data)
	return HttpResponse('Download successful')






