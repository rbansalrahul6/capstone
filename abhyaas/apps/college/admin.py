from django.contrib import admin
from .models import Branch,Department
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class BranchResource(resources.ModelResource):
	class Meta:
		model=Branch
		import_id_fields = ('branch_code',)

class BranchAdmin(ImportExportModelAdmin):
	list_display = ('branch_code','branch_name')
	resource_class=BranchResource
	
class DepartmentResource(resources.ModelResource):
	class Meta:
		model=Department
		import_id_fields = ('department_name',)

class DepartmentAdmin(ImportExportModelAdmin):
	resource_class=DepartmentResource
	


admin.site.register(Branch,BranchAdmin)
admin.site.register(Department,DepartmentAdmin)
