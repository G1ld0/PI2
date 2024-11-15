from django.shortcuts import render, redirect
from catalogo.models import Autor, Livro, InstanciaLivro
from django.views import generic
from .utils import extrair_texto_pdf, converter_para_markdown  


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
        # Iniciando a criação de um novo objeto Livro
        novo_livro = Livro()
        novo_livro.titulo = request.POST.get('titulo')
        novo_livro.autor_id = request.POST.get('autor_id')  # Supõe-se que o autor é identificado por seu ID
        novo_livro.data_publicacao = request.POST.get('data_publicacao')
        novo_livro.isbn = request.POST.get('isbn')
        novo_livro.numero_paginas = request.POST.get('numero_paginas')
        novo_livro.idioma = request.POST.get('idioma')
        
        # Processando o arquivo PDF, se fornecido
        arquivo_pdf = request.FILES.get('arquivo_pdf')
        if arquivo_pdf:
            # Extração de texto do arquivo PDF
            texto_extraido = extrair_texto_pdf(arquivo_pdf)
            if texto_extraido:  # Verifica se algum texto foi extraído com sucesso
                # Conversão do texto extraído para Markdown
                texto_markdown = converter_para_markdown(texto_extraido)
                novo_livro.conteudo_markdown = texto_markdown
            else:
                print("Não foi possível extrair texto do PDF ou o PDF está vazio.")
        
        # Salvando o novo livro no banco de dados
        novo_livro.save()
        return redirect('index')  # Redirecionar para a página inicial ou outra página conforme necessário
    else:
        # Renderizar o formulário para cadastro de livros
        return render(request, 'cadastrolivros.html')
      
def visualizar_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    return render(request, 'catalogo/visualizar_livro.html', {'livro': livro})