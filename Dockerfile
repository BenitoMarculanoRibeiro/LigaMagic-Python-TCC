# Dockerfile, Image, Conteiner

# FROM é para falar qual linguagem e versão você quer trabalhar
FROM python:3.8

# WORKDIR serve para indicar qual pasta você vai trabalhar, vale lembrar que por padrão o sistema do Docker bota o SO Ubumtu
WORKDIR /ligamagic-tcc

# COPY copia pastas e arquivos para dentro de sua area de trabalho
COPY main.py .

COPY concertar.py .

COPY teste.py .

COPY ./arquivos ./arquivos

COPY ./objetos_AG ./objetos_AG

# CMD serve para indicar quais comandos serão executados no terminal do SO Virtual
CMD ["python", "./main.py"]

# Se nescessario crie uma lista de requerimentos 
# COPY requirements.txt .

# E instale no Docker
# RUN pip install -r requirements.txt

# Crie/atualize a imagem 
# docker build -t ligamagic-tcc .

# Rode o container
# docker run ligamagic-tcc

# Limpando os container não usados:
# docker container prune
