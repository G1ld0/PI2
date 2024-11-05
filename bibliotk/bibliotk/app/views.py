from django.shortcuts import render
from .models import Livro
import markdown2

def index(request):
    """página principal de bibliotk"""
    livros = Livro.objects.all()
    for livro in livros:
        livro.conteudo_html = markdown2.markdown(livro.conteudo)
    return render(request, 'app/index.html', {'livros': livros})