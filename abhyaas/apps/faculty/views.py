from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from django.http import HttpResponse,HttpResponseRedirect
from courses.models import CourseFacultyMap
from login.models import Faculty
from faculty.forms import UploadFileForm
from courses.models import CurrentCourse,CourseNotification,CourseFacultyMap,CourseStudentMap,UploadMetadata,Assignment,AssignmentSubmission
from course_scheme.models import Subgroup
from courses import views as course_views
from login.models import Student,Faculty
from notifications.signals import notify
from django.core.urlresolvers import reverse
from django.conf import settings
import datetime
import os
import time
import dropbox
from utils.file_utils import upload_to_dropbox,check,create_folder,get_download_link,faculty_check,is_notadmin
# Create your views here.

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
@user_passes_test(faculty_check,login_url=settings.LOGIN_URL)
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
@user_passes_test(faculty_check,login_url=settings.LOGIN_URL)
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
@user_passes_test(faculty_check,login_url=settings.LOGIN_URL)
def course_page(request):
	context = RequestContext(request)
	course_page_view = course_views.index(request)
	course_page_view.render()
	data=course_page_view.context_data
	return render_to_response('faculty/course_details.html',data,context)

@login_required(login_url="/login/login/")
@user_passes_test(faculty_check,login_url=settings.LOGIN_URL)
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
@user_passes_test(faculty_check,login_url=settings.LOGIN_URL)
def upload(request):
	myfile = None
	uploaded = False
	course_code = request.GET.get('code')
	data = {'course_code':course_code}
	ccourse = CurrentCourse.objects.get(course_code=course_code)
	faculty = Faculty.objects.get(username=request.user.username)
	if request.method=='POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		filename = myfile.name
		print filename
		if myfile is not None:
			if not check(dbx,course_code):
				create_folder(dbx,course_code)
			curr_time = datetime.datetime.now()
			result = upload_to_dropbox(dbx,myfile,myfile.name,course_code,curr_time)
			metadata = UploadMetadata(uploader=faculty,course=ccourse,
				filename=myfile.name,upload_time=curr_time)
			metadata.save()
			uploaded = True
			print result
		return HttpResponseRedirect("%s?code=%s" % (reverse('faculty:coursepage'),course_code))
	else:	
		return render(request,'faculty/upload_file.html',data)	

@login_required(login_url="/login/login/")
@user_passes_test(faculty_check,login_url=settings.LOGIN_URL)
def show_announcement(request):
	context=RequestContext(request)
	course_code = request.GET.get('code')
	
	user=Faculty.objects.get(username=request.user.username)
	
	course=CurrentCourse.objects.get(course_code=course_code)
	notif=CourseNotification.objects.filter(course=course)
	ccourse=CurrentCourse.objects.get(course_code=course_code)
	#unreadlist_course,unreadlist_desc=getdesc_coursecode(user.notifications.unread().values_list('description',flat=True))
	data={"notif":notif,"course_code":course_code,"course_name":ccourse.course_name}
	return render_to_response('faculty/announcement_page.html',data,context)

# @user_passes_test(is_notadmin,login_url=settings.LOGIN_URL)
# @user_passes_test(faculty_check,login_url=settings.LOGIN_URL)
# @login_required(login_url="/login/login/")
# def show_inbox(request):
# 	context=RequestContext(request)
# 	user=Faculty.objects.get(username=request.user.username)
# 	unreadlist_course,unreadlist_desc=getdesc_coursecode(user.notifications.unread()
# 		.values_list('description',flat=True))
# 	unreadlist_otherfields=user.notifications.unread()
# 	readlist_course,readlist_desc=getdesc_coursecode(user.notifications.read()
# 		.values_list('description',flat=True))
# 	readlist_otherfields=user.notifications.read()
# 	print unreadlist_course,unreadlist_desc,unreadlist_desc
# 	# data={"notif":notif,"course_code":course_code,"course_name":ccourse.course_name}
# 	# return render_to_response('faculty/announcement_page.html',data,context)	

@login_required(login_url="/login/login/")
@user_passes_test(faculty_check,login_url=settings.LOGIN_URL)
def show_inbox(request):
	context=RequestContext(request)
	user=Faculty.objects.get(username=request.user.username)
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
	return render_to_response('faculty/inbox.html',{"unread_zip":unread_zip,"read_zip":read_zip},context)

@login_required(login_url="/login/login/")
@user_passes_test(faculty_check,login_url=settings.LOGIN_URL)
def assignments_list(request):
	course_code = request.GET.get('code')
	ccourse = CurrentCourse.objects.get(course_code=course_code)
	assignments = Assignment.objects.filter(course=ccourse)
	data = {'assgn_list':assignments,'course_code':course_code}
	return 	render(request,'faculty/list_assignments.html',data)

@login_required(login_url="/login/login/")
@user_passes_test(faculty_check,login_url=settings.LOGIN_URL)
def create_assignment(request):
	course_code = request.GET.get('code')
	data = {'course_code':course_code}
	print course_code
	afile = None
	if request.method == 'POST' and request.FILES['afile']:
 		afile = request.FILES['afile']
 		aname = request.POST['aname']
 		mmarks = request.POST['mmarks']
 		ddate = request.POST['ddate']
 		insts = request.POST['insts']
 		if afile is not None:
 			ccourse = CurrentCourse.objects.get(course_code=course_code)
			faculty = Faculty.objects.get(username=request.user.username)
			if not check(dbx,course_code):
				create_folder(dbx,course_code)
			ass_folder = os.path.join(course_code,'assignments')
			if not check(dbx,ass_folder):
				create_folder(dbx,ass_folder)
			result = result = upload_to_dropbox(dbx,afile,afile.name,course_code,datetime.datetime.now(),subfolder='assignments')
			assignment = Assignment(name=aname,course=ccourse,uploader=faculty,
				deadline=ddate,filename=afile.name,instructions=insts,max_marks=mmarks)
			assignment.save()
			print result
		return HttpResponseRedirect("%s?code=%s" % (reverse('faculty:assignments'),course_code))
	else:	
 		return render(request,'faculty/create_assignment.html',data)		

@login_required(login_url="/login/login/")
@user_passes_test(faculty_check,login_url=settings.LOGIN_URL)
def send_announcement(request):
	context=RequestContext(request)
	course_code = request.GET.get('code')
	if request.method == 'POST':
			print "here"
			subj= request.POST['subject']
			msg= request.POST['message']
			send_to= course_code
			linkedcourse=CurrentCourse.objects.get(course_code=send_to)
			CourseNotification(course=linkedcourse,
				message=subj,sender=Faculty.objects.get(username
					=request.user.username),description=msg).save()
			
			linkedbatch=CourseStudentMap.objects.filter(course=linkedcourse)
			for b in linkedbatch:
				linkedstu=Student.objects.filter(batch=b.batch,branch=b.branch)
				notify.send(request.user, recipient=linkedstu, verb=subj, description=send_to+"_"+msg)
			linkedfac=CourseFacultyMap.objects.filter(course=linkedcourse)
			for fac in linkedfac:
				notify.send(request.user, recipient=Faculty.objects.get(username=fac.faculty.username), verb=subj, description=send_to+"_"+msg)
			ccourse=CurrentCourse.objects.get(course_code=course_code)
			time.sleep(2)		
			return HttpResponseRedirect("%s?code=%s" % (reverse('faculty:coursepage'),course_code))			
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
		return render_to_response('faculty/newannounce.html',{"course_code":course_code,"course_name":ccourse.course_name},context)	


@login_required(login_url="/login/login/")
@user_passes_test(faculty_check,login_url=settings.LOGIN_URL)
def view_assignment(request):
	course_code = request.GET.get('code')
	assgn_id = request.GET.get('aid')
	assignment = Assignment.objects.get(id=assgn_id)
	alink = get_download_link(dbx,course_code,assignment.filename,'assignments')
	data = {'course_code':course_code,'assgn':assignment,'alink':alink}
	return render(request,'faculty/view_assignment.html',data)


@login_required(login_url="/login/login/")
@user_passes_test(faculty_check,login_url='/login/login/')
def evaluate_assignment(request):
	course_code=request.GET.get('code')
	aid=request.GET.get('aid')
	assignmentob=Assignment.objects.get(id=aid)
	aname=assignmentob.name
	ccourse=CurrentCourse.objects.get(course_code=course_code)
	list3=CourseStudentMap.objects.filter(course=ccourse).values_list('branch',flat=True)
	batchlist=CourseStudentMap.objects.filter(course=ccourse).values_list('batch',flat=True)
	branchlist=[]
	for i in list3:
 		branchlist.append(i.encode('utf8'))
	mixlist=zip(branchlist,batchlist)
	subgrp=[]
	for ele in mixlist:
		no=Subgroup.objects.get(branch=ele[0],batch=ele[1]).no_of_subgroups
		i=1
		while i<no+1:
			subgrp.append(ele[0]+"-"+str(i))
			i=i+1
	if request.method=='POST':
		selectgrp=request.POST['sub']
		br=selectgrp.split('-',1)[0]
		selectbatch=None;

		for ele in mixlist:
			if ele[0]==br:
				selectbatch=ele[1]
				break
		print selectgrp,selectbatch,br		
		stulist=Student.objects.filter(batch=selectbatch,subgroup=selectgrp)
		print stulist
		asslist=[]
		
		print assignmentob
		for stu in stulist:
			if AssignmentSubmission.objects.filter(student=stu,assignment=assignmentob,status='S').exists():
				asslist.append(AssignmentSubmission.objects.get(student=stu,assignment=assignmentob,status='S'))
		#print asslist,asslist[0].student.username
		return render(request,'faculty/evaluate_assignment.html',{"slist":subgrp,"assign":asslist,'course_code':course_code,'aname':aname})	
	else:	
		return render(request,'faculty/evaluate_assignment.html',{"slist":subgrp,'course_code':course_code,'aname':aname})	


def grade_assignment(request):
	course_code = request.GET.get('code')
	sub_id = request.GET.get('subid')
	asub = AssignmentSubmission.objects.get(id=sub_id)
	sfilename = asub.student.username + '|' + asub.solution_file
	slink = get_download_link(dbx,course_code,sfilename,'submissions')
	data = {'course_code':course_code,'asub':asub,'slink':slink}

	if request.method=='POST':
		marks=request.POST['marks']
		remarks=request.POST['remarks']
		asub.marks=marks
		asub.remarks=remarks
		asub.status='E'
		asub.save()
		return HttpResponseRedirect("%s?code=%s&aid=%s" % (reverse('faculty:evaluate'),course_code,sub_id))
	else:	
		return render(request,'faculty/evaluate_form.html',data)


