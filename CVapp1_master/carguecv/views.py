from django.shortcuts import render
from .models import Exp_Profesional, Formacion, Area, cv
from django.http import HttpResponseRedirect
from .forms import MovimientoCV, MovimientoExpPro
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

# Create your views here.

def carguecv(request):
    return render(request, "carguecv.html")
def cargueexplav(request):
    return render(request, "cargueexplav.html")
def Detail(request):
    return render(request, "detail.html")

def home(request):
    return render (request,"home.html")

class BadgetView(ListView):
    template_name = 'carguecv.html'
    model = cv

class BadgetViewExp(ListView):
    template_name = 'cargueexplav.html'
    model = Exp_Profesional

class CreateCV(CreateView):
    model = cv
    fields =['nombre', 'apellido', 'tipo_identificacion', 'ceduala', 'fecha_nacimiento',
    'genero', 'estado_civil', 'telefono', 'Departamento', 'direccion', 'licencia', 'foto',
    'experiencia_profesional', 'formacion', 'idioma', 'nivel', 'estado_laboral', 'area', 'salario', 'carga_cv']

    def get_success_url(self):
        return reverse('')

class BadgetUpdate(UpdateView):
    model = cv
    fields =['nombre', 'apellido', 'tipo_identificacion', 'ceduala', 'fecha_nacimiento',
    'genero', 'estado_civil', 'telefono', 'Departamento', 'direccion', 'licencia', 'foto',
    'experiencia_profesional', 'formacion', 'idioma', 'nivel', 'estado_laboral', 'area', 'salario', 'carga_cv']

    def get_success_url(self):
        return reverse('')

class BadgetDetail(DetailView):
    template_name = 'detail.html'
    model = cv
