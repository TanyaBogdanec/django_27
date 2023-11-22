from django.contrib import admin
from .models import WorkingProfile


class WorkingProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "email")
    list_filter = ("name", "email")
    search_fields = ("name", "address", "email")

admin.site.register(WorkingProfile, WorkingProfileAdmin)
