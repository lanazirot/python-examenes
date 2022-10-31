from django.contrib import admin
from django.urls import path
from webapp.views import mainView, usuarioView, reservacionView, vueloView
from Usuario.views import detalleUsuario, nuevoUsuario, eliminarUsuario, editarUsuario
from Vuelo.views import detalleVuelo, nuevoVuelo, eliminarVuelo, editarVuelo
from Reservacion.views import detalleReservacion, nuevoReservacion, eliminarReservacion, editarReservacion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainView, name='index'),

    path('lista_usuarios', usuarioView, name='usuarioList'),
    path('detalle_usuario/<int:id>', detalleUsuario),
    path('nuevo_usuario', nuevoUsuario),
    path('editar_usuario/<int:id>', editarUsuario),
    path('eliminar_usuario/<int:id>', eliminarUsuario),

    path('lista_reservaciones', reservacionView, name='reservacionList'),
    path('detalle_reservacion/<int:id>', detalleReservacion),
    path('nuevo_reservacion', nuevoReservacion),
    path('editar_reservacion/<int:id>', editarReservacion),
    path('eliminar_reservacion/<int:id>', eliminarReservacion),

    path('lista_vuelos', vueloView, name='vueloList'),
    path('detalle_vuelo/<int:id>', detalleVuelo),
    path('nuevo_vuelo', nuevoVuelo),
    path('editar_vuelo/<int:id>', editarVuelo),
    path('eliminar_vuelo/<int:id>', eliminarVuelo),
]
