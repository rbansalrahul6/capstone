from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from login.models import Student

# Create your views here.
@login_required(login_url="/login/login/")
def index(request):
	context = RequestContext(request)
	return render_to_response('students/student.html',{},context)


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