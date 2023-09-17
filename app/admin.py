from django.contrib import admin
from app.models import *
# Register your models here.

class customstudent(admin.ModelAdmin):
    list_display=['Sname','Sid','Semail']
    list_display_links=['Sid']
    list_editable=['Semail']
    # list_per_page=1
    search_fields=['Sname','Semail']


admin.site.register(Student,customstudent)