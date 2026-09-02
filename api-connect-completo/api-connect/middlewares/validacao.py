import re


def validar_usuario(dados):
    if not isinstance(dados, dict):
        return "O corpo da requisição deve ser um objeto JSON."

    nome = dados.get("nome")
    email = dados.get("email")

    if not isinstance(nome, str) or not nome.strip():
        return "O campo nome é obrigatório."

    if not isinstance(email, str) or not email.strip():
        return "O campo email é obrigatório."

    padrao_email = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"

    if not re.match(padrao_email, email.strip()):
        return "O campo email deve conter um endereço de e-mail válido."

    if "idade" in dados and dados["idade"] is not None:
        if isinstance(dados["idade"], bool) or not isinstance(dados["idade"], int):
            return "O campo idade deve ser um número inteiro."

        if dados["idade"] < 0:
            return "O campo idade não pode ser negativo."

    return None
