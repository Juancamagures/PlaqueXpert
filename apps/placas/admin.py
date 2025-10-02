from django.contrib import admin
from .models import conductor, estudiante, vehiculo, propietario, monitor, jornada, movimientos

@admin.register(conductor.Conductor)
class conductorAdmin(admin.ModelAdmin):
    list_display = ("id_conductor" , "nombres", "apellidos" , "identificacion" , "telefono", "clase_licencia")
    search_fields = ("nombre" , "identificacion")
    list_filter = ("clase_licencia",)

@admin.register(estudiante.Estudiante)
class estudianteAdmin(admin.ModelAdmin):
    list_display = ("id_Estudiante" , "nombres", "apellidos" , "identificacion" , "grado")
    search_fields = ("nombres" , "identificacion")
    list_filter = ("grado",)

@admin.register(vehiculo.Vehiculo)
class vehiculoAdmin(admin.ModelAdmin):
    list_display = ("id_vehiculo" , "nickname" , "placa" , "marca" , "modelo" , "cupos" , "propietario")
    search_fields = ("placa" , "marca" , "propietario__nombre")
    list_filter = ("marca" , "modelo")

@admin.register(movimientos.Movimientos)
class movimientoAdmin(admin.ModelAdmin):
    list_display = ("id_movimiento" , "vehiculo" , "jornada" , "monitor" , "hora_llegada" , "hora_salida" , "punto")
    search_fields = ("vehiculo__placa" , "jornada__nombre" , "estudiante__nombre")
    list_filter = ("hora_llegada" , "hora_salida"  , "jornada")

@admin.register(propietario.Propietario)
class propietarioAdmin(admin.ModelAdmin):
    list_display = ("id_propietario" , "nombres", "apellidos" , "telefono" , "correo_electronico")
    search_fields = ("nombre" ,  "telefono")

@admin.register(jornada.Jornada)
class jornadaAdmin(admin.ModelAdmin):
    list_display = ("id_jornada" , "nombre" , "inicio" , "fin")
    search_fields = ("nombre",)

@admin.register(monitor.Monitor)
class monitorAdmin(admin.ModelAdmin):
    list_display = ("monitor_id", "nombres" , "apellidos", "identificacion" , "tipo_monitor")
    search_fields = ("nombre", "identificacion")

# list_display = ("__str__",) => Define las columnas que se mostrarán en la lista de objetos. Puedes usar campos del modelo o métodos.
# list_display_links = () => Especifica qué campos de list_display serán enlaces para editar el objeto. Si está vacío, Django usará el primero.
# list_filter = () => Agrega filtros laterales para filtrar por campos específicos (como fechas, booleanos, relaciones, etc.).
# list_select_related => False	Si es True o una tupla de relaciones, usa select_related para optimizar consultas con claves foráneas.
# list_per_page = 100 => Número de objetos que se muestran por página en la lista.
# list_max_show_all = 200 => Máximo de objetos que se pueden mostrar si el usuario selecciona “Mostrar todos”.
# list_editable = () => Campos que se pueden editar directamente desde la lista sin entrar al detalle del objeto.
# search_fields = () => Campos por los que se puede buscar usando la barra de búsqueda.
# search_help_text = None => Texto de ayuda que aparece debajo del campo de búsqueda.
# date_hierarchy = None	=> Campo de tipo fecha para navegar por año/mes/día desde la parte superior.
# save_as = False	=> Si es True, permite guardar un objeto como uno nuevo desde el admin.
# save_as_continue = True => Si es True, después de guardar como nuevo, permite seguir editando el nuevo objeto.
# save_on_top = False => Si es True, muestra los botones de guardar también en la parte superior del formulario.
# paginator = Paginator	=> Clase usada para paginar los resultados. Puedes personalizarla si necesitas una paginación especial.
# preserve_filters = True	=> Si es True, mantiene los filtros aplicados al volver desde la vista de edición.
# show_facets = ShowFacets.ALLOW	=> (Desde Django 5.0) Permite mostrar filtros avanzados (facetas) si están disponibles.
# inlines = ()	Lista de clases InlineModelAdmin para mostrar modelos relacionados directamente en el formulario.


#Ejemplo de como usar los metodos relacionados con el model.Admin

# list_display_links = ("nombre", "apellido")
# list_filter = ("especialidad", "estado", "fecha_ingreso")
# list_select_related = False
# list_per_page = 25
# list_max_show_all = 100
# list_editable = ("estado",)
# search_fields = ("nombre", "apellido", "correo", "especialidad")
# search_help_text = "Buscar por nombre, apellido, correo o especialidad"
# date_hierarchy = "fecha_ingreso"
# save_as = True
# save_as_continue = True
# save_on_top = True
# preserve_filters = True
# inlines = ()  # Modelos relacionados