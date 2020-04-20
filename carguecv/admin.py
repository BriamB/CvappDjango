from django.contrib import admin
from .models import Departamento, Municipio, Area, Tipo_Identificacion, Cargo, carga_cv

# Register your models here.
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(Area)
admin.site.register(carga_cv)
admin.site.register(Cargo)
