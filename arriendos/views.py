from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from arriendos.forms import InmuebleForm, RegistroUsuarioForm
from arriendos.models import Inmueble, Solicitud, Usuario




class RegistroUsuarioView(CreateView):
    model = Usuario
    form_class = RegistroUsuarioForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')

class DashboardArrendador(LoginRequiredMixin, ListView):
    model = Inmueble
    template_name = 'arriendos/dashboard.html'

    def get_queryset(self):
        return Inmueble.objects.filter(arrendador=self.request.user)

class CrearInmueble(LoginRequiredMixin, CreateView):
    model = Inmueble
    form_class = InmuebleForm
    template_name = 'arriendos/inmueble_form.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.arrendador = self.request.user
        return super().form_valid(form)

class EditarInmueble(LoginRequiredMixin, UpdateView):
    model = Inmueble
    form_class = InmuebleForm
    template_name = 'arriendos/inmueble_form.html'
    success_url = reverse_lazy('dashboard')

class EliminarInmueble(LoginRequiredMixin, DeleteView):
    model = Inmueble
    template_name = 'arriendos/inmueble_confirm_delete.html'
    success_url = reverse_lazy('dashboard')

class CatalogoInmuebles(ListView):
    model = Inmueble
    template_name = 'arriendos/catalogo.html'
    context_object_name = 'inmuebles'

    def get_queryset(self):
        comuna = self.request.GET.get('comuna')
        if (comuna):
            return Inmueble.objects.filter(comuna__iconstains=comuna)
        return Inmueble.objects.all()

@login_required
def generar_solicitud(request, pk):
    inmueble = get_object_or_404(Inmueble, pk=pk)
    if request.user.tipo_usuario == 'arrendatario':
        Solicitud.objects.get_or_create(arrendatario=request.user, inmueble=inmueble)
    return redirect('catalogo')

@login_required
def aceptar_solicitud(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk, inmueble__arrendador=request.user)
    solicitud.estado = 'aceptada'
    solicitud.save()
    return redirect('dashboard')