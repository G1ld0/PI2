from django.shortcuts import render, redirect
from catalogo.models import Autor, Livro, InstanciaLivro
from django.views import generic
import markdown2
import PyPDF2


# Create your views here.
def index(request):
   
    num_livros = Livro.objects.all().count()
    num_instancias = InstanciaLivro.objects.all().count()
    num_autores = Autor.objects.count()
    
    context = {
        'num_books': num_livros,
        'num_instances': num_instancias,
        'num_autores': num_autores,
    }
    return render(request, 'index.html', context=context)    

class ListaLivrosView(generic.ListView):
    model = Livro
    
def cadastrolivros(request):
    if request.method == 'POST':
        novo_livro = Livro()
        novo_livro.titulo = request.POST.get('titulo')
        novo_livro.autor_id = request.POST.get('autor_id')  # Supondo que o autor é identificado por seu ID
        novo_livro.data_publicacao = request.POST.get('data_publicacao')
        novo_livro.isbn = request.POST.get('isbn')
        novo_livro.numero_paginas = request.POST.get('numero_paginas')
        novo_livro.idioma = request.POST.get('idioma')
        novo_livro.arquivo_pdf = request.FILES.get('arquivo_pdf')

        if novo_livro.arquivo_pdf:  # Verifica se um arquivo foi realmente enviado
            texto_extraido = extrair_texto_pdf(novo_livro.arquivo_pdf)
            novo_livro.conteudo = converter_para_markdown(texto_extraido)
        
        novo_livro.save()
        return redirect('index')  # Substitua com o nome da URL para redirecionar
    else:
        return render(request, 'cadastrolivros.html')