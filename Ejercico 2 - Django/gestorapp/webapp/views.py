from django.shortcuts import render
from Usuario.models import Usuario
from Vuelo.models import Vuelo
from Reservacion.models import Reservacion

def mainView(req):
    return render(req, 'index.html');

def usuarioView(req):
    usuarios = Usuario.objects.order_by('id');
    return render(req, 'usuariosList.html', {'usuarios':usuarios});

def vueloView(req):
    vuelos = Vuelo.objects.order_by('id');
    return render(req, 'vuelosList.html', {'vuelos':vuelos});

def reservacionView(req):
    reservaciones = Reservacion.objects.order_by('id');
    return render(req, 'reservacionList.html', {'reservaciones':reservaciones});