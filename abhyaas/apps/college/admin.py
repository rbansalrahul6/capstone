from django.contrib import admin
from .models import Branch,Department
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class BranchResource(resources.ModelResource):
	class Meta:
		model=Branch

class BranchAdmin(ImportExportModelAdmin):
	list_display = ('branch_code','branch_name')
	resource_class=BranchResource
	#import_id_fields = ('id',)
	#exclude=('id',)
	#skip_unchanged= True
	#fields=['branch_code','branch_name',]

class DepartmentResource(resources.ModelResource):
	class Meta:
		model=Department

class DepartmentAdmin(ImportExportModelAdmin):
	resource_class=DepartmentResource
	import_id_fields = ('department_name',)


admin.site.register(Branch,BranchAdmin)
admin.site.register(Department,DepartmentAdmin)
