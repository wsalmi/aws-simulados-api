# Dockerfile para Backend Flask
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copia arquivos de dependências
COPY requirements.txt .

# Instala dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia código da aplicação
COPY . .

# Cria diretório para banco de dados
RUN mkdir -p src/database

# Inicializa banco de dados
RUN python init_db.py

# Define permissões para o diretório do banco de dados
RUN chmod -R 777 src/database

# Expõe porta
EXPOSE 5001

# Define variáveis de ambiente
ENV FLASK_APP=src/main.py
ENV FLASK_ENV=development
ENV PYTHONPATH=/app

# Ensure we run as root to avoid permission issues with mounted volumes
USER root

# Comando para iniciar aplicação
CMD ["python", "src/main.py"]

