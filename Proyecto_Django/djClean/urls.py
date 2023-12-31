"""djClean URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import inicio, resumen
from django.urls import re_path
from django.views.static import serve
from django.conf import settings
from rest_framework.documentation import include_docs_urls
from . import views
from aplicaciones.cursos import views as cursos_views
from aplicaciones.cursos.views import lista_certificaciones_cursos

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", inicio),
    path("inicio/", inicio, name="inicio"),
    path("resumen/", resumen, name="resumen"),
    path("accounts/", include('django.contrib.auth.urls')), 
    path("", include('aplicaciones.proyectos.urls')),
    path("", include('aplicaciones.contacto.urls')),
    path("", include('aplicaciones.ubicaciones.urls')),
    path("api/v1/", include('aplicaciones.directorio.urls')),
    path("docs/", include_docs_urls(title='Api Documentation')),  
    path('cursos/', include('aplicaciones.cursos.urls')), 
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    
]
