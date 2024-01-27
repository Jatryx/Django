from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('inicio', views.inicio, name='inicio'),
    path('empleados', views.empleados, name='empleados'),
    path('empleados/crear', views.crear, name='crear'),
    path('empleados/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('empleados/editar/<int:id>', views.editar, name='editar')

]