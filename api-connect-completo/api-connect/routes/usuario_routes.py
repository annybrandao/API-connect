from flask import Blueprint

from controllers.usuario_controller import (
    listar_usuarios,
    cadastrar_usuario,
    buscar_usuario,
    atualizar_usuario,
    remover_usuario,
)

usuario_routes = Blueprint("usuario_routes", __name__)

usuario_routes.route("/usuarios", methods=["GET"])(listar_usuarios)
usuario_routes.route("/usuarios", methods=["POST"])(cadastrar_usuario)
usuario_routes.route("/usuarios/<int:id>", methods=["GET"])(buscar_usuario)
usuario_routes.route("/usuarios/<int:id>", methods=["PUT"])(atualizar_usuario)
usuario_routes.route("/usuarios/<int:id>", methods=["DELETE"])(remover_usuario)
