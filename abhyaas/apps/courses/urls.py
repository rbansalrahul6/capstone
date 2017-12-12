from django.conf.urls import url
from . import views
urlpatterns =[url(r'^viewannouncement/$',views.view_announcement,name='viewannounce'),
url(r'^viewmessage/$',views.view_message,name='viewmessage'),
]