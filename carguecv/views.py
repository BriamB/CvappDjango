from django.shortcuts import render
from .models import Area, carga_cv
from django.http import HttpResponseRedirect
#from .forms import MovimientoCV
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

#Login requerido
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.

def carguecv(request):
    return render(request, "carguecv.html")
def Detail(request):
    return render(request, "detail.html")

def home(request):
    print(request.POST)
    return render (request,"home.html")

#Clase para listar con autenticacion
class BadgetView(LoginRequiredMixin, ListView):
    template_name = 'carguecv.html'
    model = carga_cv
    paginate_by = 10
    ordering =['cedula']

#Clase para crear
class CreateCV(CreateView):
    model = carga_cv
    success_url = reverse_lazy('carguecv')
    fields = '__all__'

#Clase para actualizar datos
class BadgetUpdate(UpdateView):
    model = carga_cv
    success_url = reverse_lazy('carguecv')
    fields = '__all__'

#Clase para ver los detalles
class BadgetDetail(DetailView):
    model = carga_cv

    def get_success_url(self):
        return reverse('')

#Metodo de busqueda
def searchMovie(request):
    if request.method == 'POST':
        pattern = request.POST['search']
        carga = carga_cv.objects.filter(estado=True, name__contains=pattern)
    else:
        carga = carga_cv.objects.filter(estado=True)
    return render(request, 'carga_search.html', {'object_list':carga, 'search':pattern})
