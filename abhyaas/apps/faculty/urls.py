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
	url(r'^inbox/$',views.show_inbox,name='showinbox'),
	
	#url(r'^sendannouncement/$',views.send_announcement,name='sendannouncement'),
]