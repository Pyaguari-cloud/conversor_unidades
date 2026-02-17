from django.contrib import admin
from django.db.models import Count
from conversor.models import Especialidad, Magnitud, Unidad
from .utils import CONVERSION_FUNCTIONS


# Personalizar el sitio admin
admin.site.site_header = "🔄 Conversor Universal - Panel Admin"
admin.site.site_title = "Conversor Admin"
admin.site.index_title = "Gestión del Sistema"


@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ("nombre", "slug", "total_magnitudes")
    list_display_links = ("nombre",)
    search_fields = ("nombre", "slug")
    prepopulated_fields = {"slug": ("nombre",)}
    
    def total_magnitudes(self, obj):
        return obj.magnitudes.count()
    total_magnitudes.short_description = "Magnitudes"


@admin.register(Magnitud)
class MagnitudAdmin(admin.ModelAdmin):
    list_display = ("nombre", "especialidad", "codigo_calculo", "total_unidades")
    list_filter = ("especialidad",)
    search_fields = ("nombre", "especialidad__nombre", "codigo_calculo")
    
    def total_unidades(self, obj):
        return obj.unidades.count()
    total_unidades.short_description = "Unidades"

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        from django import forms
        if db_field.name == "codigo_calculo":
            choices = [(k, k) for k in CONVERSION_FUNCTIONS.keys()]
            kwargs["widget"] = forms.Select(choices=choices)
        return super().formfield_for_dbfield(db_field, request, **kwargs)


@admin.register(Unidad)
class UnidadAdmin(admin.ModelAdmin):
    list_display = ("nombre", "simbolo", "magnitud", "especialidad_nombre")
    list_filter = ("magnitud__especialidad", "magnitud")
    search_fields = ("nombre", "simbolo", "magnitud__nombre")
    
    def especialidad_nombre(self, obj):
        return obj.magnitud.especialidad.nombre
    especialidad_nombre.short_description = "Especialidad"