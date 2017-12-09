from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^profile/$',views.get_profile,name='profile'),
	url(r'^mycourses/$',views.show_courses,name='showcourses'),
	url(r'^sendnotification/$',views.send_notification,name='sendnotification'),

]