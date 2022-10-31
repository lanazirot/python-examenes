from django.shortcuts import get_object_or_404, redirect, render
from Reservacion.forms import ReservacionForm
from Reservacion.models import Reservacion

def detalleReservacion(req, id) :
    reservacion = get_object_or_404(Reservacion, pk = id);
    return render(req, 'DetalleReservacion.html', {'reservacion': reservacion});

def nuevoReservacion(req) :
    if req.method == "POST":
        formaReservacion = ReservacionForm(req.POST);

        if formaReservacion.is_valid():
            formaReservacion.save();
            return redirect('reservacionList');
    else:
        formaReservacion = ReservacionForm();
        return render(req, 'AgregarReservacion.html', {'formaReservacion': formaReservacion})

def editarReservacion(req, id):
    reservacion = get_object_or_404(Reservacion, pk = id);
    if req.method == "POST":
        formaReservacion = ReservacionForm(req.POST, instance = reservacion);

        if formaReservacion.is_valid():
            formaReservacion.save();
            return redirect('reservacionList');
    else:
        formaReservacion = ReservacionForm(instance = reservacion);
        return render(req, 'EditarReservacion.html', {'formaReservacion': formaReservacion})

def eliminarReservacion(req, id):
    reservacion = get_object_or_404(Reservacion, pk = id);
    if reservacion:
        reservacion.delete();
        return redirect('reservacionList');