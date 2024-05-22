from django.shortcuts import render
from rest_framework import generics
from .models import Evento
from .serializers import EventoSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# Create your views here.
class EventoListCreate(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class EventoRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer