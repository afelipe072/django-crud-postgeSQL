"""CRUDOperation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from CRUDOperation.views import showemp, insertEmp, editarEmp, actualizarEmp,eliminar

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^inicio/',showemp, name="showemp"),    
    url(r'^insertar/',insertEmp, name="insertEmp"),
    url(r'editar/(?P<id>\d+)',editarEmp, name="editarEmp"),
    url(r'actualizar/(?P<id>\d+)',actualizarEmp,name="actualizarEmp"),
    url(r'eliminar/(?P<id>\d+)',eliminar, name="eliminar")
    
]
