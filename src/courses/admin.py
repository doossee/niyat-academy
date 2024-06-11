from django.contrib import admin
from .models import Course, Module, Content



@admin.register(Course)
class SubjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Module)
admin.site.register(Content)
