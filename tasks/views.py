from rest_framework import viewsets, permissions
from tasks.models import Task
from .serializers import TaskSerializer
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from rest_framework.authtoken.views import ObtainAuthToken,APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('index')
    else:
        form = form()
    return render(request, 'tasks/create_task.html', {'form': form})

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:   
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form, 'task_id': pk})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request, 'tasks/confirm_delete_task.html', {'task': task})

def finalizar_tarefa(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.finalizada = True
    task.save()
    return redirect('index')

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})