from django.contrib import admin
from Usuario.models import Usuario
from Vuelo.models import Vuelo
from Vuelo.models import Ciudad
from Reservacion.models import Reservacion
from Reservacion.models import Pasajero

admin.site.register(Usuario);
admin.site.register(Vuelo);
admin.site.register(Reservacion);
admin.site.register(Pasajero);
admin.site.register(Ciudad);