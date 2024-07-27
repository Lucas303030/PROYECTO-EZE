from django.contrib import admin
from .models import Empresa, Pieza, Tracking

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'direccion', 'telefono')
    search_fields = ('nombre', 'email')
    list_filter = ('nombre',)

class PiezaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'empresa')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('nombre',)

class TrackingAdmin(admin.ModelAdmin):
    list_display = ('pieza', 'fecha_actualizacion', 'origen', 'destino','estado')
    search_fields = ('pieza__nombre', 'estado')
    list_filter = ('pieza__nombre', 'estado')

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Pieza, PiezaAdmin)
admin.site.register(Tracking, TrackingAdmin)