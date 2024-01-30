from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EventoForm
from .models import Evento
from datetime import datetime

# Create your views here.

def index(request):
    eventos = Evento.objects.filter(fecha__gte=datetime.today()).order_by('fecha')
    context = {'eventos': eventos}
    
    return render(request, 'home.html', context)

@login_required
def create_event_view(request):
    context = {}

    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.organizador = request.user
            form.save()
            return redirect('home')
        else:
            context['form'] = form

    else:
        form = EventoForm()
        context['form'] = form
    
    return render(request, 'CreateEvent.html', context)