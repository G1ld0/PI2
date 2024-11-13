from django.urls import path
from . import views
from .views import pdf_to_markdown_view, upload_livro_view


urlpatterns = [
    path('', views.index,  name='index'),
    path('upload_livro/', upload_livro_view, name='upload_livro'),
    path('pdf_to_markdown/', pdf_to_markdown_view, name='pdf_to_markdown'),

]
