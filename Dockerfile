# Imagem oficial do Python, versão slim (leve)
FROM python:3.12-slim

# Sem .pyc e com log sem buffer (aparece na hora no `docker logs`)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MOCHILA_DB=/app/data/mochila_cheia.db

WORKDIR /app

# Dependências primeiro: enquanto o requirements.txt não mudar, o Docker
# reaproveita esta camada do cache e o build fica rápido
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Resto do código (o .dockerignore deixa de fora venv, testes, docs e o banco local)
COPY . .

# Usuário sem privilégio de root, dono só das pastas que a app escreve
RUN useradd --create-home mochila \
    && mkdir -p /app/data src/web/static/uploads \
    && chown -R mochila /app/data src/web/static/uploads
USER mochila

EXPOSE 5000

# O Docker consulta a rota /api/saude para saber se a app está de pé
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:5000/api/saude')"

ENTRYPOINT ["docker/entrypoint.sh"]
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "src.web:create_app('production')"]
