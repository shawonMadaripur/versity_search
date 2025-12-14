from django.contrib import admin
from .models import AllList
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.register(AllList, ImportExportModelAdmin)