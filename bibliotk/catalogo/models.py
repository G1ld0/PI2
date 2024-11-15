from django.db import models
from django.urls import reverse


"""Autores dos livros"""
class Autor(models.Model):
    primeiro_nome = models.CharField(max_length=100)  # Nome do autor do livro
    sobrenome = models.CharField(max_length=100)  # Sobrenome do autor do livro

    class Meta:
        ordering = ['primeiro_nome', 'sobrenome']

    def get_absolute_url(self):
        """Retorna a URL para acessar uma instância específica do autor."""
        return reverse('detalhes-autor', args=[str(self.id)])

    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return f'{self.primeiro_nome}, {self.sobrenome}'


"""Livros de domínio público"""
class Livro(models.Model):
    titulo = models.CharField(max_length=200)  # Título do livro
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True)
    data_publicacao = models.DateField()  # Data de publicação do livro
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn" target="_blank" rel="noopener noreferrer">Site do ISBN</a>')  # ISBN do livro (deve ser único)
    numero_paginas = models.PositiveIntegerField()  # Número de páginas do livro
    idioma = models.CharField(max_length=30)  # Idioma do livro
    conteudo_markdown = models.TextField(blank=True, null=True)  # Conteúdo do livro em markdown

    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return self.titulo

    def get_absolute_url(self):
        """Retorna a URL para acessar um registro detalhado deste livro."""
        return reverse('book-detail', args=[str(self.id)])


"""Página Sobre"""
class PaginaSobre(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


import uuid

class InstanciaLivro(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID exclusivo para este livro específico em toda a biblioteca')
    livro = models.ForeignKey('Livro', on_delete=models.CASCADE)
    imprint = models.CharField(max_length=200)

    def __str__(self):
        """String para representar o objeto Model."""
        return f'{self.id} ({self.livro.titulo})'
    
