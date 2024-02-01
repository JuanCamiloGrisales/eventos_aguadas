from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    # path('create_event', create_event_view, name='create_event'),
    path('mis_eventos', mis_eventos_view, name='mis_eventos'),
    path('evento/<int:id>', evento_edit, name='evento'),
    path('evento/<int:id>/delete', delete_evento, name='eliminar_evento'),
    path('evento/<int:id>/asistir', asistir_a_evento, name='asistir'),
    path('evento/<int:id>/dejar_de_asistir', dejar_de_asistir_a_evento, name='dejar_de_asistir'),
]