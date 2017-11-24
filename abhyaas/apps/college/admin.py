from django.contrib import admin
from .models import Branch,Department
# Register your models here.

class BranchAdmin(admin.ModelAdmin):
	list_display = ('branch_code','branch_name')

admin.site.register(Branch,BranchAdmin)
admin.site.register(Department)
