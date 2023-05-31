from django.db.models import fields
from rest_framework import serializers
from app.tarea.models import Tareas

class TareaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields=('id','descripcion')

