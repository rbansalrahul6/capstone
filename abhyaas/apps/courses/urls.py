from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^download/$',views.download_file,name='download'),
	]