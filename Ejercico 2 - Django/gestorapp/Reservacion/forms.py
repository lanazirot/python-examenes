from django.forms import ModelForm
from Reservacion.models import Reservacion

class ReservacionForm(ModelForm):
    class Meta:
        model = Reservacion;
        fields = '__all__';