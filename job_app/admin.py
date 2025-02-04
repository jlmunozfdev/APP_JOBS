from django.contrib import admin
from .models import JobApplication

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company_name', 'application_date', 'closing_date', 'status',)
    search_fields = ('job_title', 'company_name', 'application_date', 'closing_date', 'status',)
    list_filter = ('status',)
    

admin.site.register(JobApplication, JobAdmin)