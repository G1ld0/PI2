# Generated by Django 5.1.3 on 2024-11-15 04:29

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['primeiro_nome', 'sobrenome'],
            },
        ),
        migrations.CreateModel(
            name='PaginaSobre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('conteudo', models.TextField()),
                ('ultima_atualizacao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('data_publicacao', models.DateField()),
                ('isbn', models.CharField(help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN</a>', max_length=13, verbose_name='ISBN')),
                ('numero_paginas', models.PositiveIntegerField()),
                ('idioma', models.CharField(max_length=30)),
                ('conteudo', models.TextField()),
                ('arquivo_pdf', models.FileField(blank=True, null=True, upload_to='livros_pdfs/')),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.autor')),
            ],
        ),
        migrations.CreateModel(
            name='InstanciaLivro',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID exclusivo para este livro específico em toda a biblioteca', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('livro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.livro')),
            ],
        ),
    ]
