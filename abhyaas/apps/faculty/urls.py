from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.show_courses,name='index'),
	url(r'^profile/$',views.get_profile,name='profile'),
	url(r'^mycourses/$',views.show_courses,name='showcourses'),
	url(r'^course_page/$',views.course_page,name='coursepage'),
	url(r'^upload/$',views.upload,name='upload'),
	url(r'^announcement/$',views.show_announcement,name='showannouncement'),
	url(r'^newannouncement/$',views.send_announcement,name='newannouncement'),
	url(r'^assignments/$',views.assignments_list,name='assignments'),
	url(r'^new_assignment/$',views.create_assignment,name='create_assignment'),
	url(r'^view_assignment/$',views.view_assignment,name='view_assignment'),
	url(r'^evaluate_assignment/$',views.evaluate_assignment,name='evaluate')
	#url(r'^sendannouncement/$',views.send_announcement,name='sendannouncement'),
]