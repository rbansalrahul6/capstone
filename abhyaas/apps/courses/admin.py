from django.contrib import admin
from .models import CurrentCourse,CourseStudentMap,CourseFacultyMap,CourseNotification,Assignment,AssignmentSubmission

# Register your models here.
admin.site.register(CurrentCourse)
admin.site.register(CourseStudentMap)
admin.site.register(CourseFacultyMap)
admin.site.register(CourseNotification)
admin.site.register(Assignment)
admin.site.register(AssignmentSubmission)