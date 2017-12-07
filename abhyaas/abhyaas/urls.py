from django.conf.urls import patterns, include, url
from django.contrib import admin
from login.views import logout_view


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'abhyaas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/',include('login.urls')),
    url(r'^student/',include('students.urls')),
    url(r'^faculty/',include('faculty.urls')),
    url(r'^messages/', include('django_messages.urls')),
    url(r'^synch/',include('testapp.urls')),
    url(r'logout/',logout_view,name='logout_the_user'),
)
