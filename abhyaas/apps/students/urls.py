from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.show_courses,name='index'),
	url(r'^profile/$',views.get_profile,name='profile'),
	url(r'^mycourses/$',views.show_courses,name='showcourses'),
	url(r'^course_page/$',views.course_page,name='coursepage'),
	url(r'^assignments/$',views.show_assignments,name='assignments'),
	url(r'^submit_assignment/$',views.submit_assignment,name='submit_assignment')
]