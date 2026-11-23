from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):

    list_display = (
        'company_name',
        'job_title',
        'location',
        'applied_date',
        'status',
    )

    list_filter = ('status', 'job_type')

    search_fields = ('company_name', 'job_title')