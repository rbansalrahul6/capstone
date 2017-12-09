from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from .forms import UploadFileForm
import dropbox
from utils.file_utils import check,list_files
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


def upload_file(request):
	file_name = request.GET.get('filename')
	course_code = request.GET.get('code')
	if not check(dbx,course_code):
		create_folder(dbx,course_code)

	result = upload(dbx=dbx,fullname=file_name,folder=course_code,name=file_name)
	print result
	return HttpResponse('Successfully uploaded')

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

def upload_test(request):
	if request.method=='POST':
		upload_form = UploadFileForm(data=request.POST)
		if upload_form.is_valid():
			# process upload_from.cleaned_data
			return 
	else:
		upload_form = UploadFileForm()
	data = {'upload_form':upload_form}
	return TemplateResponse(request,'courses/upload_file.html',data)






