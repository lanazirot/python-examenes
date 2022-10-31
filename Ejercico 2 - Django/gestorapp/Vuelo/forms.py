from django.forms import ModelForm, DateInput
from Vuelo.models import Vuelo

class VueloForm(ModelForm):
    class Meta:
        model = Vuelo;
        fields = '__all__';
        widgets = {
            'fecha': DateInput(attrs={'type': 'date'}),
        };