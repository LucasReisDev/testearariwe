from django.db import models
from django.forms import model_to_dict
from rest_framework import serializers

from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'titulo', 'prazo', 'descricao', 'finalizada')
