from flask import jsonify, request

from data.usuario_data import carregar_usuarios, gerar_id, salvar_usuarios
from middlewares.validacao import validar_usuario


def listar_usuarios():
    usuarios = carregar_usuarios()
    return jsonify({"data": usuarios}), 200


def cadastrar_usuario():
    dados = request.get_json(silent=True)

    erro = validar_usuario(dados)
    if erro:
        return jsonify({"error": erro}), 400

    usuarios = carregar_usuarios()
    email = dados["email"].strip().lower()

    if any(usuario["email"].lower() == email for usuario in usuarios):
        return jsonify({
            "error": "O e-mail informado já está cadastrado."
        }), 400

    novo_usuario = {
        "id": gerar_id(usuarios),
        "nome": dados["nome"].strip(),
        "email": email,
    }

    if "idade" in dados and dados["idade"] is not None:
        novo_usuario["idade"] = dados["idade"]

    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)

    return jsonify({"data": novo_usuario}), 201


def buscar_usuario(id):
    usuarios = carregar_usuarios()

    usuario = next(
        (usuario for usuario in usuarios if usuario["id"] == id),
        None
    )

    if usuario is None:
        return jsonify({"error": "Usuário não encontrado."}), 404

    return jsonify({"data": usuario}), 200


def atualizar_usuario(id):
    usuarios = carregar_usuarios()

    indice = next(
        (
            indice
            for indice, usuario in enumerate(usuarios)
            if usuario["id"] == id
        ),
        None
    )

    if indice is None:
        return jsonify({"error": "Usuário não encontrado."}), 404

    dados = request.get_json(silent=True)

    erro = validar_usuario(dados)
    if erro:
        return jsonify({"error": erro}), 400

    email = dados["email"].strip().lower()

    email_em_uso = any(
        usuario["email"].lower() == email and usuario["id"] != id
        for usuario in usuarios
    )

    if email_em_uso:
        return jsonify({
            "error": "O e-mail informado já está cadastrado por outro usuário."
        }), 400

    usuario_atualizado = {
        "id": id,
        "nome": dados["nome"].strip(),
        "email": email,
    }

    if "idade" in dados and dados["idade"] is not None:
        usuario_atualizado["idade"] = dados["idade"]

    usuarios[indice] = usuario_atualizado
    salvar_usuarios(usuarios)

    return jsonify({"data": usuario_atualizado}), 200


def remover_usuario(id):
    usuarios = carregar_usuarios()

    indice = next(
        (
            indice
            for indice, usuario in enumerate(usuarios)
            if usuario["id"] == id
        ),
        None
    )

    if indice is None:
        return jsonify({"error": "Usuário não encontrado."}), 404

    usuarios.pop(indice)
    salvar_usuarios(usuarios)

    return "", 204
