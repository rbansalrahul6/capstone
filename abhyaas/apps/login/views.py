from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext,loader
from django.contrib.auth import authenticate,login
# Create your views here.


def index(request):
	return HttpResponse('welcome')


def user_login(request):
	context = RequestContext(request)

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		#attempt to authenticate
		user = authenticate(username=username,password=password)
		#if correct details
		if user:
			if user.is_active:
				login(request,user)
				return HttpResponse('success')
			else:
				return HttpResponse('account disabled')
		else:
			#bad login details
			return HttpResponse('invalid login details')

	else:
		#not a POST request, display login form
		return render_to_response('login/login.html',{},context)
