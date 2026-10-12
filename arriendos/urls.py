from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.CatalogoInmuebles.as_view(), name='catalogo'),
    path('registro/', views.RegistroUsuarioView.as_view(), name='registro'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Arrendador
    path('dashboard/', views.DashboardArrendador.as_view(), name='dashboard'),
    path('inmueble/crear/', views.CrearInmueble.as_view(), name='crear_inmueble'),
    path('inmueble/editar/<int:pk>/', views.EditarInmueble.as_view(), name='editar_inmueble'),
    path('inmueble/eliminar/<int:pk>/', views.EliminarInmueble.as_view(), name='eliminar_inmueble'),
    path('solicitud/aceptar/<int:pk>/', views.aceptar_solicitud, name='aceptar_solicitud'),

    # Arrendatario
    path('solicitar/<int:pk>/', views.generar_solicitud, name='generar_solicitud'),
]