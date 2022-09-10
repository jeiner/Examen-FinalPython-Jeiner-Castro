
from django.urls import path
from . import views


urlpatterns = [
    path('listar-todos/', views.listar_meseros_view, name='listar-todos/'),
]