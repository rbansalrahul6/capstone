from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.text import force_text
from .models import Course,CourseItem,CourseScheme,FacultyMapping
# Register your models here.

class CourseItemInline(admin.StackedInline):
	model = CourseItem
	extra = 0
	fields = ['get_edit_link','course','course_type','remarks']
	readonly_fields = ['get_edit_link']

	def get_edit_link(self,obj=None):
		if obj.pk:
			url = reverse('admin:%s_%s_change' % (obj._meta.app_label,obj._meta.model_name),args=[force_text(obj.pk)])
			return """<a href="{url}">{text}</a>""".format(
				url=url,
				text=_("Edit this %s separately") % obj._meta.verbose_name,
				)
		return _("(save and continue editing to create a link)")
	get_edit_link.short_description = _("Edit link")
	get_edit_link.allow_tags = True

class FacultyInline(admin.StackedInline):
	model = FacultyMapping
	extra = 0
	fields = ['faculty']

class CourseSchemeAdmin(admin.ModelAdmin):
	save_on_top = True
	fields = ['batch','semester','branch']
	inlines = [CourseItemInline]

class CourseItemAdmin(admin.ModelAdmin):
	save_on_top = True
	fields = ['course_scheme','course','course_type','remarks','is_current']
	inlines = [FacultyInline]


admin.site.register(Course)
admin.site.register(CourseItem,CourseItemAdmin)
admin.site.register(CourseScheme,CourseSchemeAdmin)
admin.site.register(FacultyMapping)