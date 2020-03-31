from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static #busca archivos
from django.conf import settings

#views applications
from carguecv import views

urlpatterns = [
    path('', views.home, name=""),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include(('users.urls','users'), namespace='users')),
    path('carguecv/',views.BadgetView.as_view(), name='carguecv'),
    path('cargueexplav/',views.BadgetViewExp.as_view(), name='cargueexplav'),
    path('<int:pk>', views.BadgetUpdate.as_view(), name='editar'),
    path('<int:pk>',views.BadgetDetail.as_view(), name='Detail'),
    path('crear/', views.CreateCV.as_view(), name="crear"),
    path('users/', include(('users.urls', 'users'), namespace='users')),

]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
