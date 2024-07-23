# Usando uma imagem base do Python
FROM python:3.10-slim

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando os arquivos necessários para o contêiner
COPY . /app

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Comando para executar o script Python
CMD ["python", "carregamento.py"]
