from django.contrib import admin
from django.db import models
from .models import CurrentCourse,CourseStudentMap,CourseFacultyMap,CourseNotification,UploadMetadata,Assignment,AssignmentSubmission

class CurrentCourseAdmin(admin.ModelAdmin):
	list_display = ['course_code','course_name']

class CourseStudentMapAdmin(admin.ModelAdmin):	
	list_display = ['course','branch','batch']

class CourseFacultyMapAdmin(admin.ModelAdmin):	
	list_display = ['course','faculty']	

class UploadMetadataAdmin(admin.ModelAdmin):	
	list_display = ['course','filename','uploader']	

class CourseNotificationAdmin(admin.ModelAdmin):	
	list_display = ['course','message','description','sender','time']	

class AssignmentAdmin(admin.ModelAdmin):	
	list_display = ['name','course','uploader','deadline','filename']	

class AssignmentSubmissionAdmin(admin.ModelAdmin):	
	list_display = ['assignment','student','solution_file','submit_date','status']	


# Register your models here.
admin.site.register(CurrentCourse,CurrentCourseAdmin)
admin.site.register(CourseStudentMap,CourseStudentMapAdmin)
admin.site.register(CourseFacultyMap,CourseFacultyMapAdmin)
admin.site.register(CourseNotification,CourseNotificationAdmin)
admin.site.register(UploadMetadata,UploadMetadataAdmin)
admin.site.register(Assignment,AssignmentAdmin)
admin.site.register(AssignmentSubmission,AssignmentSubmissionAdmin)
