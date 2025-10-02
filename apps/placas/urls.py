from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.placas.views.vehiculo import VehiculoViewSet
from apps.placas.views.propietario import PropietarioViewSet
from apps.placas.views.movimientos import MovimientoViewSet
from apps.placas.views.monitor import MonitorViewSet
from apps.placas.views.jornada import JornadaViewSet
from apps.placas.views.estudiante import EstudianteViewSet
from apps.placas.views.conductor import ConductorViewSet

router = DefaultRouter()
router.register(r'vehiculos', VehiculoViewSet, basename='vehiculo')
router.register(r'propietarios', PropietarioViewSet, basename='propietario')
router.register(r'movimientos', MovimientoViewSet, basename='movimiento')
router.register(r'monitores', MonitorViewSet, basename='monitor')
router.register(r'jornadas', JornadaViewSet, basename='jornada')
router.register(r'estudiantes', EstudianteViewSet, basename='estudiante')
router.register(r'conductores', ConductorViewSet, basename='conductor')

urlpatterns = [
    path('api/', include(router.urls)),
]