"""
URL configuration for bibliotk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from catalogo import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalogo/', include('catalogo.urls')),
    path('', RedirectView.as_view(url='/catalogo/')),
    path('livros/', views.ListaLivrosView.as_view(), name='livros'),
    path('cadastrolivros/', views.cadastrolivros, name='cadastrolivros'),
    path('livros/<int:livro_id>/', views.visualizar_livro, name='visualizar_livro'),

]