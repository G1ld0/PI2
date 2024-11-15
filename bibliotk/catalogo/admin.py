from django.contrib import admin
from catalogo.models import Autor, Livro, InstanciaLivro

admin.site.register(Livro)
admin.site.register(Autor)
admin.site.register(InstanciaLivro)