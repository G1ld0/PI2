# Versão do Python leve
FROM python:3.9-alpine3.13

# copiando os requirements para dentro de um diretório temporário no container
COPY ./requirements.txt /tmp/requirements.txt
# copiando a raiz do nosso projeto e setando como raiz dentro do container
COPY . /bibliotk
WORKDIR /bibliotk


# disponibilizando a porta para acessar o container via browser
EXPOSE 8000

    # criando ambiente virtual dentro do container
    # atualizando gerenciador de pacotes do python: pip
    # instalando client e pacote de desenvolvimento do postgresql
    # instalando as bibliotecas e dependencias especificadas em requirements
    # deletando as pastas temporarias após instalar para não desperdiçar espaço
    # criando usuário do sistema para não usar o root, pois não é aconselhável por questões de segurança
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client jpeg-dev zlib-dev libjpeg && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

# garantindo que quando algo for executado, deverá primeiramente ser procurado o ambiente virtual
# (ordem de prioridade de execução container)
ENV PATH="/py/bin:$PATH"

# setando usuário que não pode criar pastas e tem senha desabilitada
USER django-user

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]