from django.shortcuts import render
from django.views.decorators.http import require_http_methods


# Create your views here.
from apps.meseros.models import Mesero


def listar_meseros_view(request):
    meseros = Mesero.objects.filter(procedencia='peru').all()
    return render(request, 'resources/meseros/index.html', {'meseros': meseros})
