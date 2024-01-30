from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('create_event', create_event_view, name='create_event'),
]