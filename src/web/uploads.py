"""
Upload de imagens (infra) - Mochila Cheia

Salva a foto enviada no formulário de publicação/edição em static/uploads e
devolve o caminho público para gravar em ITEM.foto_url. Mantém o tratamento de
arquivos isolado dos controllers.

Responsável: Júlio (Backend)
"""

import os
import uuid
from typing import Optional

from flask import current_app
from werkzeug.utils import secure_filename


def _extensao_permitida(nome: str) -> bool:
    return "." in nome and nome.rsplit(".", 1)[1].lower() in \
        current_app.config["EXTENSOES_IMAGEM"]


def salvar_foto(arquivo) -> Optional[str]:
    """
    Salva o arquivo enviado (FileStorage) e retorna o caminho público
    (ex.: /static/uploads/abc.jpg) ou None se não houver arquivo válido.
    """
    if arquivo is None or not arquivo.filename:
        return None
    if not _extensao_permitida(arquivo.filename):
        return None

    pasta = current_app.config["UPLOAD_FOLDER"]
    os.makedirs(pasta, exist_ok=True)

    ext = secure_filename(arquivo.filename).rsplit(".", 1)[1].lower()
    nome = f"{uuid.uuid4().hex}.{ext}"
    arquivo.save(os.path.join(pasta, nome))
    return f"/static/uploads/{nome}"
