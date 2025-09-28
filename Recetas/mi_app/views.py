from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView, TemplateView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Receta
from .forms import ContactoForm

def index(request):
    ultimas = Receta.objects.order_by('-id')[:3] 
    return render(request, 'index.html', {'ultimas': ultimas})

def receta(request):
    recetas = Receta.objects.all()
    return render(request, 'receta.html', {'recetas': recetas})

def receta_detalle(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    return render(request, 'recetas/detalle.html', {'receta': receta})

class ContactoView(FormView):
    template_name = 'contacto.html'
    form_class = ContactoForm
    success_url = reverse_lazy('mi_app:contacto_ok')

    def form_valid(self, form):
        messages.success(self.request, 'Tu mensaje fue enviado con éxito.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Por favor completa el formulario correctamente.')
        return super().form_invalid(form)

class ContactoOKView(TemplateView):
    template_name = 'contacto_ok.html'

def error_404_view(request, exception):
    return render(request, '404.html', status=404)