from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings

# Create your views here.
@login_required
def index(request):
	context = RequestContext(request)
	return render_to_response('students/student.html',{},context)