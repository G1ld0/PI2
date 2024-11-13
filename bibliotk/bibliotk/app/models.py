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
    arquivo_pdf = models.FileField(upload_to='livros_pdfs/', blank=True, null=True)  # opcionalmente, você pode permitir arquivos em branco


    def __str__(self):
        """Devolve uma representação em string do modelo"""
        return self.titulo

"""Status de leitura do livro"""
class StatusLeitura(models.Model):
    STATUS_CHOICES = [
        ('NL', 'Não Lido'),
        ('LE', 'Lendo'),
        ('LI', 'Lido'),
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='NL')

    def __str__(self):
        return self.get_status_display()

"""Registro de leitura do usuário"""
class RegistroLeitura(models.Model):
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    status = models.ForeignKey(StatusLeitura, on_delete=models.CASCADE)
    data_inicio = models.DateField(null=True, blank=True)
    data_conclusao = models.DateField(null=True, blank=True)
    ultima_pagina_lida = models.PositiveIntegerField(default=0)
    nota = models.PositiveSmallIntegerField(null=True, blank=True, choices=[(i,i) for i in range(1,6)])
    comentario = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ['usuario', 'livro']

    def __str__(self):
        return f"{self.usuario.username} - {self.livro.titulo}"

"""Página Sobre"""
class PaginaSobre(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

"""Página Principal"""
class PaginaPrincipal(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo