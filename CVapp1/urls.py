from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static #busca archivos
from django.conf import settings #Importar contenido del settings

#views applications
from carguecv import views

urlpatterns = [
    #Ruta principal
    path('', views.home, name=""),
    path('admin/', admin.site.urls),
    #Ruta de user
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include(('users.urls','users'), namespace='users')),
    #Ruta de las vistas hojas de vida
    path('carguecv/',views.BadgetView.as_view(), name='carguecv'),
    #Ruta de modificacion
    path('<int:pk>', views.BadgetUpdate.as_view(), name='editar'),
    #Ruta de detalles
    path('detail/<int:pk>',views.BadgetDetail.as_view(), name='detail'),
    #Ruta de creación
    path('crear/', views.CreateCV.as_view(), name="crear"),
    #Ruta de uusuarios
    path('users/', include(('users.urls', 'users'), namespace='users')),
    #Ruta de busqueda
    path('buscar/', views.searchMovie, name='buscar'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
