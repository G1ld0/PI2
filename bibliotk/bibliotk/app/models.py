from django.db import models

"""Autores dos livros"""
class Autor(models.Model):
    nome = models.CharField(max_length=100)  # Nome do autor do livro
    biografia = models.TextField(blank=True, null=True)  # Biografia do autor (opcional)

    class Meta:
        verbose_name_plural = 'Autores'

    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return self.nome

"""Livros de domínio público"""
class Livro(models.Model):
    titulo = models.CharField(max_length=200)  # Título do livro
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='livros')  # Autor do livro (relação com o modelo Autor)
    data_publicacao = models.DateField()  # Data de publicação do livro
    isbn = models.CharField(max_length=13, unique=True)  # ISBN do livro (deve ser único)
    numero_paginas = models.PositiveIntegerField()  # Número de páginas do livro
    imagem_capa = models.ImageField(upload_to='capas/', blank=True, null=True)  # Imagem da capa do livro (opcional)
    idioma = models.CharField(max_length=30)  # Idioma do livro
    conteudo = models.TextField()  # Conteúdo do livro (texto completo)

    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return self.titulo
