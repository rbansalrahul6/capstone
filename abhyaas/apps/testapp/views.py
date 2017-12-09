from django.shortcuts import render
from course_scheme.models import Course,CourseScheme,CourseItem,FacultyMapping
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from courses.models import CourseFacultyMap,CourseStudentMap,CurrentCourse
import datetime
from django.template import RequestContext
# Create your views here.
def currentsem(batch):
	curr_year = datetime.datetime.now().year
	curr_month=datetime.datetime.now().month
	sem=(curr_year-batch)*2
	if curr_month>6 and curr_month<=12:
		sem=sem+1;
	return sem


def synch(request):
	context = RequestContext(request)
	print "synch running"
	year_choices = []
	curr = datetime.datetime.now().year
	for y in range(curr-4,curr+1):
		year_choices.append(y)
	for y in year_choices:
		sem=currentsem(y)
		synch_course_schemes=CourseScheme.objects.filter(batch=y,semester=sem)
		for curr_scheme in synch_course_schemes:
			print curr_scheme
			synch_courseitem=CourseItem.objects.filter(course_scheme=curr_scheme,is_current=False)
			for curr_courseitem in synch_courseitem:
				ccobject=CurrentCourse(course_code=
						curr_courseitem.course.course_code,course_name=
						curr_courseitem.course.course_name)
				if not CurrentCourse.objects.filter(course_code=curr_courseitem.course.course_code).exists():
					print "course added"
					ccobject.save()

				csm=CourseStudentMap(course=ccobject,batch=
					curr_courseitem.course_scheme.batch,branch=
					curr_courseitem.course_scheme.branch)

				if not CourseStudentMap.objects.filter(course=ccobject,batch=
					curr_courseitem.course_scheme.batch,branch=
					curr_courseitem.course_scheme.branch).exists():
						csm.save()

				faculties=FacultyMapping.objects.filter(course_item=curr_courseitem)
				for curr_faculty in faculties:
					cfm=CourseFacultyMap(course=ccobject,faculty=curr_faculty.faculty)
					if not CourseFacultyMap.objects.filter(course=ccobject,
						faculty=curr_faculty.faculty).exists():
							cfm.save()

				curr_courseitem.is_current=True
				curr_courseitem.save()			

				




				#CourseStudentMap.create(cou)
	return HttpResponseRedirect("/synch/")
		#currcourse=CourseItem.objects.filter()	

def index(request):
	context = RequestContext(request)
	return render_to_response('testapp/testapp.html',{},context)		
