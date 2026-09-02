import json
import os

ARQUIVO = os.path.join(os.path.dirname(__file__), "usuarios.json")


def carregar_usuarios():
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_usuarios(usuarios):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, ensure_ascii=False, indent=4)


def gerar_id(usuarios):
    if not usuarios:
        return 1

    return max(usuario["id"] for usuario in usuarios) + 1
