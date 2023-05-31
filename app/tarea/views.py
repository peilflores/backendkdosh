from rest_framework import viewsets
from .serializers import TareaSerializers
from app.tarea.models import Tareas

class TareaViewSet(viewsets.ModelViewSet):

    queryset = Tareas.objects.all()
    serializer_class =TareaSerializers
