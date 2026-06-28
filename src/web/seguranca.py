"""
Segurança de senhas (infra) - Mochila Cheia

Centraliza o hash e a verificação de senhas. Cadastros novos usam bcrypt
(salting + key derivation), conforme decisão documentada no relatório. Mantém
compatibilidade com os usuários de exemplo do seed, cujas senhas foram geradas
com SHA-256 nas etapas anteriores do projeto — assim o login funciona tanto
para contas novas quanto para a base de demonstração.
"""

import hashlib

import bcrypt


def gerar_hash_senha(senha: str) -> str:
    """Gera o hash bcrypt de uma senha em texto plano."""
    return bcrypt.hashpw(senha.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verificar_senha(senha: str, hash_armazenado: str) -> bool:
    """
    Confere se a senha corresponde ao hash guardado no banco.

    Detecta o algoritmo pelo prefixo do hash: bcrypt (contas novas) ou o
    SHA-256 legado dos usuários de exemplo do seed.
    """
    if not senha or not hash_armazenado:
        return False

    if hash_armazenado.startswith("$2"):  # bcrypt ($2a$ / $2b$ / $2y$)
        try:
            return bcrypt.checkpw(senha.encode("utf-8"), hash_armazenado.encode("utf-8"))
        except ValueError:
            return False

    # Compatibilidade com a base de exemplo (SHA-256)
    return hashlib.sha256(senha.encode("utf-8")).hexdigest() == hash_armazenado
