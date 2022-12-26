"""proyecto001 URL Configuration

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
from django.urls import path
from miapp import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.cursos, name = "cursos"),
    path('cursos/', views.cursos, name = "cursos"),
    path('crear_cursos/',views.crear_cursos, name = "crear_cursos"),
    path('carreras/',views.carreras,name="carreras"),
    path('rango2/<int:a>/<int:b>',views.rango2,name="rango2"),
    path('crear-articulo/<str:titulo>/<str:contenido>/<str:publicado>',views.crear_articulo,name="crear_articulo"),
    path('buscar-articulo', views.buscar_articulo, name="buscar_articulo"),
    path('editar-articulo/<int:id>',views.editar_articulo,name="editar_articulo"),
    path('listar-articulos/',views.listar_articulos,name="listar_articulos"),
    path('crear_carreras/',views.crear_carreras, name='crear_carreras'),
]