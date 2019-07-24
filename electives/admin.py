from django.contrib import admin
from .models import Elective, Comment
from import_export.admin import ImportExportModelAdmin
from .models import Elective
from .resources import ElectiveResource


@admin.register(Elective)
class ElectiveAdmin(ImportExportModelAdmin):
    resource_class = ElectiveResource
    list_display = ('id', 'name', 'professor', 'credit', 'school', 'cross')

admin.site.register(Comment)
