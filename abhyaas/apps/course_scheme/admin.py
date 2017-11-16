from django.contrib import admin
from .models import Course,CourseScheme
# Register your models here.
class CourseInline(admin.StackedInline):
	model = CourseScheme.courses.through

class CourseSchemeAdmin(admin.ModelAdmin):
	inlines = [
		CourseInline,
	]
	exclude = ('courses',)


admin.site.register(Course)
admin.site.register(CourseScheme,CourseSchemeAdmin)
