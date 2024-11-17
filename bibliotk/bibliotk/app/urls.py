from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo,  name='catalogo'),
    path('meuslivros', views.meuslivros,  name='meuslivros'),
    path('catalogo', views.catalogo, name='catalogo'),
    path('sobre', views.sobre, name='sobre')
]
