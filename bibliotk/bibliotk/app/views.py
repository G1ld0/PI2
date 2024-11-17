from django.shortcuts import render
from .models import Livro, PaginaSobre
from django.shortcuts import get_object_or_404
import markdown2

def meuslivros(request):
    """página principal de bibliotk"""
    livro_id = request.GET.get('id')
    if livro_id:
        livro = get_object_or_404(Livro, id=livro_id)
        livro.conteudo_html = markdown2.markdown(livro.conteudo)
        return render(request, 'app/meuslivros.html', {'livros': [livro]})  # Passa uma lista com o livro
    else:
        livros = Livro.objects.all()
        for livro in livros:
            livro.conteudo_html = markdown2.markdown(livro.conteudo)
        return render(request, 'app/meuslivros.html', {'livros': livros})

def catalogo(request):
    """Mostra todos os livros da biblioteca"""
    livros = Livro.objects.order_by('titulo')
    context = {'livros': livros}
    return render(request, 'app/catalogo.html', context)

def sobre(request):
    """Informações sobre o projeto"""
    sobre = PaginaSobre.objects.first()
    context = {'sobre': sobre}
    return render(request, 'app/sobre.html', context)