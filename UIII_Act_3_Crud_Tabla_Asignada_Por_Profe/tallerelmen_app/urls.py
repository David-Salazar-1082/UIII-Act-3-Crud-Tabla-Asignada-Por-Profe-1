from django.urls import path
from tallerelmen_app import views

urlpatterns = [
    path('', views.inicio_vista, name='inicio_vista'),
    path('registrarProducto/', views.registrarProducto, name='registrarProducto'),
    path("seleccionarProducto/<Id_Producto>",views.seleccionarProducto,name="seleccionarProducto"),
    path("editarProducto/",views.editarProducto,name="editarProducto"),
    path("borrarProducto/<Id_Producto>" ,views.borrarProducto,name="borrarProducto")

]