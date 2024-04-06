from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from . import views

# Crie um DefaultRouter
router = DefaultRouter()

# Registre sua TaskViewSet
router.register(r'tasks', TaskViewSet)

# Defina suas URLs
urlpatterns = [
    # Inclua as URLs da API REST da TaskViewSet
    path('', views.index, name='index'),
    path('criar/', views.create_task, name='criar_tarefa'),
    path('editar/<int:pk>/', views.edit_task, name='editar_tarefa'),
    path('excluir/<int:pk>/', views.delete_task, name='excluir_tarefa'),
    path('finalizar/<int:pk>/', views.finalizar_tarefa, name='finalizar_tarefa'),
]

# Inclua as URLs geradas pelo DefaultRouter
urlpatterns += router.urls