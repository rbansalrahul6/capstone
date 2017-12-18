from django.conf.urls import patterns, include, url
from django.contrib import admin
from login.views import logout_view
import notifications.urls

admin.site.site_header='Abhyaas admin'
admin.site.site_title='Abhyaas admin'
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'abhyaas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/',include('login.urls')),
    url(r'^student/',include('students.urls',namespace="students")),
    url(r'^faculty/',include('faculty.urls', namespace="faculty")),
    url(r'^synch/',include('testapp.urls')),
    url(r'^courses/',include('courses.urls',namespace="courses")),
    url(r'logout/',logout_view,name='logout_the_user'),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications'))
)
