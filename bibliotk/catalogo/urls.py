from django.urls import path
from catalogo import views


urlpatterns = [
    path('', views.index, name='index'),
    path('livros/', views.ListaLivrosView.as_view(), name='livros'),
    path('cadastrolivros/', views.cadastrolivros, name='cadastrolivros'),
]
