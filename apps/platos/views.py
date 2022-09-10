from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets
from rest_framework.decorators import action
from django.http import JsonResponse
from rest_framework import status

from apps.platos.models import Plato
# Create your views here.


def listar_platillos_view(request):
    platos = Plato.objects.all()
    return render(request, 'resources/platos/index.html', {'platos': platos})


@require_http_methods(["POST"])
def crear_plato_view(request):
    plato = Plato()
    plato.nombre = request.POST.get('nombre')
    plato.precio = request.POST.get('precio')
    plato.procedencia = request.POST.get('procedencia')
    plato.save()

    return redirect('listar-todos-platos')


@require_http_methods(["GET"])
def buscar_plato_html(request):
    return render(request, 'resources/platos/buscar.html')


@require_http_methods(["GET"])
def show_edit_page(request, id_plato):
    plato = Plato.objects.filter(id=id_plato).first()
    return render(request, 'resources/platos/edit.html', {'plato': plato})


class PlatoViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['put'])
    def update_plato(self, request, id_plato):
        plato = Plato.objects.filter(id=id_plato).first()

        if plato is not None:
            plato.nombre = request.data.get('nombre')
            plato.precio = request.data.get('precio')
            plato.procedencia = request.data.get('procedencia')
            plato.save()

        return JsonResponse({'status': 'ok', 'message': 'se Actualizó correctamente'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def listar_plato_by_id(self, request, id_plato):
        plato = Plato.objects.filter(id=id_plato).first()

        return JsonResponse({'status': 'ok', 'plato': model_to_dict(plato)}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['delete'])
    def eliminar_plato_id(self, request, id_plato):
        plato = Plato.objects.filter(id=id_plato).first()

        if plato is not None:
            plato.delete()

        return JsonResponse({'status': 'ok', 'plato': 'El plato se elimino correctamente'}, status=status.HTTP_200_OK)

