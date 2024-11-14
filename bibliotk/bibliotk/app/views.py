# em bibliotk/views.py
from django.shortcuts import render, redirect
from .models import Livro
import markdown2
from .utilitarias import extrair_texto_pdf, converter_para_markdown

def index(request):
    """ Página principal de bibliotk """
    livros = Livro.objects.all()
    for livro in livros:
        livro.conteudo_html = markdown2.markdown(livro.conteudo)
    return render(request, 'app/index.html', {'livros': livros})

def pdf_to_markdown_view(request):
    """ Processa um arquivo PDF enviado e retorna Markdown """
    if request.method == 'POST':
        pdf_file = request.FILES.get('file')
        if pdf_file:
            texto_extraido = extrair_texto_pdf(pdf_file)
            markdown = converter_para_markdown(texto_extraido)
            return render(request, 'app/display_markdown.html', {'markdown': markdown})
        else:
            return render(request, 'app/upload_form.html', {'error': 'Nenhum arquivo enviado.'})
    else:
        return render(request, 'app/upload_form.html')
  
def upload_livro_view(request):
    if request.method == 'POST':
        novo_livro = Livro()
        novo_livro.titulo = request.POST.get('titulo')
        novo_livro.autor_id = request.POST.get('autor_id')  # Supondo que o autor é identificado por seu ID
        novo_livro.data_publicacao = request.POST.get('data_publicacao')
        novo_livro.isbn = request.POST.get('isbn')
        novo_livro.numero_paginas = request.POST.get('numero_paginas')
        novo_livro.imagem_capa = request.FILES.get('imagem_capa')
        novo_livro.idioma = request.POST.get('idioma')
        novo_livro.arquivo_pdf = request.FILES.get('arquivo_pdf')

        if novo_livro.arquivo_pdf:  # Verifica se um arquivo foi realmente enviado
            texto_extraido = extrair_texto_pdf(novo_livro.arquivo_pdf)
            novo_livro.conteudo = converter_para_markdown(texto_extraido)
        
        novo_livro.save()
        return redirect('index')  # Substitua com o nome da URL para redirecionar
    else:
        return render(request, 'app/upload.html')    