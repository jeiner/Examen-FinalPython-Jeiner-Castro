
from django.urls import path
from . import views


urlpatterns = [
    path('listar-platos/', views.listar_platillos_view, name='listar-todos-platos'),
    path('buscar-plato/', views.buscar_plato_html, name='buscar-plato'),
    # Mostrar formulario de actualizacion
    path('editar-plato/<int:id_plato>', views.show_edit_page, name='editar-plato/<int:id_plato>'),
    # Actualizar datos de plato
    path('update/<int:id_plato>', views.PlatoViewSet.as_view({'put': 'update_plato'}), name='update/<int:id_plato>'),
    path('listar/<int:id_plato>', views.PlatoViewSet.as_view({'get': 'listar_plato_by_id'}), name='listar/<int:id_plato>'),
    path('eliminar/<int:id_plato>', views.PlatoViewSet.as_view({'delete': 'eliminar_plato_id'}), name='eliminar/<int:id_plato>'),

]