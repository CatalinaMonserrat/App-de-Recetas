from django.shortcuts import render, get_object_or_404, redirect
from .models import Receta
from django.contrib import messages
from .forms import ContactoForm

def index(request):
    ultimas = Receta.objects.order_by('-id')[:3]
    return render(request, 'index.html', {'ultimas': ultimas})

def receta(request):
    recetas = Receta.objects.all()
    return render(request, 'receta.html', {'recetas': recetas})

def contacto(request):
    return render(request, 'contacto.html')

def receta_detalle(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    return render(request, 'recetas/detalle.html', {'receta': receta})

def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            messages.success(request, "Tu mensaje ha sido enviado con éxito.")
            return redirect("mi_app:contacto")
    else:
        form = ContactoForm()
    return render(request, "contacto.html", {"form": form})