# Generated by Django 5.1.3 on 2024-11-13 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_paginaprincipal_paginasobre_registroleitura_statusleitura'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='arquivo_pdf',
            field=models.FileField(blank=True, null=True, upload_to='livros_pdfs/'),
        ),
    ]
