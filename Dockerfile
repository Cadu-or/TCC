# Usa a imagem base do Python 3.12
FROM python:3.12-slim

# Instalar dependências de compilação
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    make \
    && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . .

# Copia os arquivos de requisitos para o container e instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta onde o Django vai rodar
EXPOSE 8000

# Define o script de inicialização para rodar migrações antes de subir o servidor
ENTRYPOINT ["sh", "/app/entrypoint.sh"]
