from django.shortcuts import get_object_or_404, redirect, render
from Vuelo.forms import VueloForm
from Vuelo.models import Vuelo

def detalleVuelo(req, id) :
    vuelo = get_object_or_404(Vuelo, pk = id);
    return render(req, 'DetalleVuelo.html', {'vuelo': vuelo});

def nuevoVuelo(req) :
    if req.method == "POST":
        formaVuelo = VueloForm(req.POST);

        if formaVuelo.is_valid():
            formaVuelo.save();
            return redirect('vueloList');
    else:
        formaVuelo = VueloForm();
        return render(req, 'AgregarVuelo.html', {'formaVuelo': formaVuelo})

def editarVuelo(req, id):
    vuelo = get_object_or_404(Vuelo, pk = id);
    if req.method == "POST":
        formaVuelo = VueloForm(req.POST, instance = vuelo);

        if formaVuelo.is_valid():
            formaVuelo.save();
            return redirect('vueloList');
    else:
        formaVuelo = VueloForm(instance = vuelo);
        return render(req, 'EditarVuelo.html', {'formaVuelo': formaVuelo})

def eliminarVuelo(req, id):
    vuelo = get_object_or_404(Vuelo, pk = id);
    if vuelo:
        vuelo.delete();
        return redirect('vueloList');