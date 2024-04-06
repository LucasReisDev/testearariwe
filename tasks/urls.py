from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CustomAuthToken, TaskViewSet
from . import views
from rest_framework.routers import DefaultRouter

# Crie um DefaultRouter para as tarefas
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

# Crie outro DefaultRouter para a autenticação
auth_router = DefaultRouter()
auth_router.register(r'auth', CustomAuthToken, basename='auth')

urlpatterns = [
    # Inclua as URLs da API REST da TaskViewSet
    path('', views.index, name='index'),
    path('criar/', views.create_task, name='criar_tarefa'),
    path('editar/<int:pk>/', views.edit_task, name='editar_tarefa'),
    path('excluir/<int:pk>/', views.delete_task, name='excluir_tarefa'),
    path('finalizar/<int:pk>/', views.finalizar_tarefa, name='finalizar_tarefa'),
    path('token/', CustomAuthToken.as_view(), name='token_obtain_pair')
]

# Adicione as URLs dos roteadores aos urlpatterns
urlpatterns += router.urls
