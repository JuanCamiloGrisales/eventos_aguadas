from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):

    class Meta:
        model = Evento
        exclude = ('organizador', 'cupos', 'asistentes')
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'desde': forms.TimeInput(attrs={'type': 'time'}),
            'hasta': forms.TimeInput(attrs={'type': 'time'}),
        }