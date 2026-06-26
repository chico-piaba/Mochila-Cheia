"""
Ponto de entrada do MVP Web - Mochila Cheia
===========================================

Cria a aplicação via app factory e a expõe como `app` para o servidor de
desenvolvimento do Flask.

Como executar:

    pip install -r requirements.txt
    flask --app run init-db        # (re)cria o banco e carrega dados de exemplo
    flask --app run run --debug    # sobe o servidor em http://127.0.0.1:5000

    # ou, diretamente:
    python run.py
"""

from src.web import create_app

app = create_app("development")


if __name__ == "__main__":
    app.run(debug=True)
