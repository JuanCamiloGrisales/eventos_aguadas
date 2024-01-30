from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(EventoForm, self).__init__(*args, **kwargs)
        self.fields['titulo'].label = 'Título del Evento'
        self.fields['fecha'].label = 'Fecha del Evento'
        self.fields['fecha'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['desde'].label = 'Hora de Inicio'
        self.fields['desde'].widget = forms.TimeInput(attrs={'type': 'time'})
        self.fields['hasta'].label = 'Hora de Finalización'
        self.fields['hasta'].widget = forms.TimeInput(attrs={'type': 'time'})
        self.fields['todo_el_dia'].label = 'Todo el día'
        self.fields['lugar'].label = 'Lugar del Evento'
        self.fields['cupos_maximos'].label = 'Máximo de Cupos'
        self.fields['cupos_ilimitados'].label = 'Cupos Ilimitados'
        self.fields['precio'].label = 'Precio'
        self.fields['imagen'].label = 'Imagen del Evento'
        self.fields['adicional'].label = 'Información Adicional'

    class Meta:
        model = Evento
        exclude = ('organizador', 'cupos')
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'desde': forms.TimeInput(attrs={'type': 'time'}),
            'hasta': forms.TimeInput(attrs={'type': 'time'}),
        }

    def save(self, commit=True):
        evento = super(EventoForm, self).save(commit=False)
        if self.user:
            evento.organizador = self.user
        if commit:
            evento.save()
        return evento