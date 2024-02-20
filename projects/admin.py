from django.contrib import admin
from .models import Project, Review, Tag
from import_export.admin import ImportExportModelAdmin 


class ReviewAdmin(admin.TabularInline):
    model = Review

class ProjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = [ReviewAdmin]
    list_display = ['id', 'owner', 'title','project_image', 'created']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Review)
admin.site.register(Tag)
