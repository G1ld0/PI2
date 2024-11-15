import markdown2
import PyPDF2

def extrair_texto_pdf(arquivo_pdf):
    texto_completo = ''
    try:
        pdf_reader = PyPDF2.PdfReader(arquivo_pdf)
        for pagina in pdf_reader.pages:
            texto_completo += pagina.extract_text()
    except PyPDF2.errors.PdfReadError:
        print("Erro na leitura do PDF")
    return texto_completo

def converter_para_markdown(texto):
    return markdown2.markdown(texto)