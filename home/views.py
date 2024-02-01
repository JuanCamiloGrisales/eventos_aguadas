from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EventoForm
from .models import Evento
from datetime import datetime

# Create your views here.

def index(request):
    eventos = Evento.objects.filter(fecha__gte=datetime.today()).order_by('fecha')
    context = {'messages': [], 
                'eventos': eventos}

    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        try:

            if form.is_valid():
                form.instance.organizador = request.user
                form.save()
                context['messages'].append('Evento creado exitosamente, puedes ver tus eventos en el apartado "Mis eventos"')

                return redirect('home')
            else:
                context['form'] = form
        
        except Exception as e:
            print(e)
            context['error_message'] = 'No se pudo crear el evento'

    else:
        form = EventoForm()
        context['form'] = form

    
    return render(request, 'home.html', context)

@login_required
def mis_eventos_view(request):
    eventos = Evento.objects.filter(organizador=request.user).order_by('fecha')
    context = {'eventos': eventos}
    return render(request, 'mis_eventos.html', context)

def evento_edit(request, id):
    evento = get_object_or_404(Evento, id=id)

    # Verificar si el usuario es el organizador del evento
    if evento.organizador != request.user:
        return render(request, 'evento.html', {'organizador': False, 'evento': evento})

    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES, instance=evento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Evento editado exitosamente.')
        else:
            messages.error(request, 'No se pudo editar el evento. Por favor, corrige los errores en el formulario.')
    else:
        form = EventoForm(instance=evento)

    return render(request, 'evento.html', {'form': form, 'organizador': True, 'evento': evento})


@login_required
def delete_evento(request, id):
    evento = Evento.objects.get(id=id)
    if evento.organizador == request.user:
        evento.delete()
        messages.success(request, 'Evento eliminado exitosamente')
        return redirect('mis_eventos')
    else:
        return redirect('evento', id=id)

@login_required
def asistir_a_evento(request, id):
    evento = Evento.objects.get(id=id)
    usuario = request.user
    if evento.cupos_ilimitados == False:
        if int(evento.cupos) >= int(evento.cupos_maximos) :
            messages.error(request, 'No hay cupos disponibles')
            return redirect('evento', id=id)
    evento.asistentes.add(usuario)
    evento.cupos += 1
    evento.save()
    return redirect('evento', id=id)

@login_required
def dejar_de_asistir_a_evento(request, id):
    evento = Evento.objects.get(id=id)
    usuario = request.user
    evento.asistentes.remove(usuario)
    evento.cupos -= 1
    evento.save()
    return redirect('evento', id=id)