from django.contrib import admin

# Register your models here.
from django.conf.locale.sr import formats as sr_formats

sr_formats.DATETIME_FORMAT = "d M Y H:i:s"
# from django.contrib.auth.models import Fugro
from .resources import FugroResource
from .models import Utilisation, Project, Car, Fugro, Author
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from import_export import resources

@admin.register(Fugro)
class FugroAdmin(ImportExportModelAdmin):
    resource_class = FugroResource


class FurgoResources(resources.ModelResource):

    class Meta:
        model = Fugro


admin.site.register(Utilisation)
admin.site.register(Car)
admin.site.register(Project)
admin.site.register(Author)
