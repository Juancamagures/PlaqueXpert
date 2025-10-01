from django.contrib import admin

from .models import ( 
    conductor,
    estudiante,
    jornada,
    monitor,
    movimientos,
    propietario,
    vehiculo
)
# Register your models here.


from .models import conductor, estudiante, vehiculo, propietario, monitor, jornada, movimientos

@admin.register(conductor)
class conductorAdmin(admin.ModelAdmin):
    list_display = ("id_conductor" , "nombres", "apellidos" , "identificacion" , "telefono", "clase_licencia")
    search_fields = ("nombre" , "identificacion")
    list_filter = ("clase_licencia",)

@admin.register(estudiante)
class estudianteAdmin(admin.ModelAdmin):
    list_display = ("id_Estudiante" , "nombres", "apellidos" , "identificacion" , "grado")
    search_fields = ("nombres" , "identificacion")
    list_filter = ("grado",)

@admin.register(vehiculo)
class vehiculoAdmin(admin.ModelAdmin):
    list_display = ("id_vehiculo" , "nickname" , "placa" , "marca" , "modelo" , "cupos" , "propietario")
    search_fields = ("placa" , "marca" , "propietario__nombre")
    list_filter = ("marca" , "modelo")

@admin.register(movimientos)
class movimientoAdmin(admin.ModelAdmin):
    list_display = ("id_movimiento" , "vehiculo" , "jornada" , "monitor" , "fecha" , "hora_llegada" , "hora_salida" , "punto")
    search_fields = ("vehiculo__placa" , "jornada__nombre" , "estudiante__nombre")
    list_filter = ("fecha" , "jornada")

@admin.register(propietario)
class propietarioAdmin(admin.ModelAdmin):
    list_display = ("id_propietario" , "nombres", "apellidos" , "telefono" , "correo_electronico")
    search_fields = ("nombre" ,  "telefono")

@admin.register(jornada)
class jornadaAdmin(admin.ModelAdmin):
    list_display = ("id_jornada" , "nombre" , "inicio" , "fin")
    search_fields = ("nombre",)

@admin.register(monitor)
class monitorAdmin(admin.ModelAdmin):
    list_display = ("monitor_id", "nombres" , "apellidos", "identificacion" , "tipo_monitor")
    search_fields = ("nombre", "identificacion")
