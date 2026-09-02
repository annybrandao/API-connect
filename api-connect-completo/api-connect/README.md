# API Connect - Gerenciamento de Usuários

## Objetivo

A API Connect é uma API REST desenvolvida para o gerenciamento de usuários. O projeto permite realizar operações de cadastro, consulta, atualização e remoção de usuários utilizando o protocolo HTTP e respostas estruturadas em formato JSON.

A aplicação foi desenvolvida como um Produto Mínimo Viável (MVP), utilizando um arquivo JSON como mecanismo de persistência provisória.

## Tecnologias utilizadas

- Python
- Flask
- JSON
- Git
- GitHub
- Postman ou Thunder Client para testes

## Estrutura do projeto

```text
api-connect/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── routes/
│   └── usuario_routes.py
├── controllers/
│   └── usuario_controller.py
├── middlewares/
│   └── validacao.py
└── data/
    ├── usuarios.json
    └── usuario_data.py
```

## Como executar localmente

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

A API ficará disponível em `http://127.0.0.1:5000`.

## Endpoints

| Método | Endpoint | Descrição | Status |
|---|---|---|---|
| GET | `/usuarios` | Lista todos os usuários | 200 |
| GET | `/usuarios/<id>` | Busca usuário por ID | 200 |
| POST | `/usuarios` | Cadastra um usuário | 201 |
| PUT | `/usuarios/<id>` | Atualiza um usuário | 200 |
| DELETE | `/usuarios/<id>` | Remove um usuário | 204 |

## Exemplo de cadastro

```http
POST http://127.0.0.1:5000/usuarios
Content-Type: application/json
```

```json
{
    "nome": "João Silva",
    "email": "joao@email.com",
    "idade": 25
}
```

Resposta `201 Created`:

```json
{
    "data": {
        "id": 1,
        "nome": "João Silva",
        "email": "joao@email.com",
        "idade": 25
    }
}
```

## Exemplo de listagem

```http
GET http://127.0.0.1:5000/usuarios
```

Resposta `200 OK`:

```json
{
    "data": [
        {
            "id": 1,
            "nome": "João Silva",
            "email": "joao@email.com",
            "idade": 25
        }
    ]
}
```

## Exemplo de busca por ID

```http
GET http://127.0.0.1:5000/usuarios/1
```

Se o usuário existir, a API retorna `200 OK`.

Se o usuário não existir:

```json
{
    "error": "Usuário não encontrado."
}
```

Status: `404 Not Found`.

## Exemplo de atualização

```http
PUT http://127.0.0.1:5000/usuarios/1
Content-Type: application/json
```

```json
{
    "nome": "João Oliveira",
    "email": "joao2@email.com",
    "idade": 26
}
```

Status: `200 OK`.

## Exemplo de remoção

```http
DELETE http://127.0.0.1:5000/usuarios/1
```

Status: `204 No Content`.

## Validações

Os campos `nome` e `email` são obrigatórios nas operações de cadastro e atualização. O e-mail também precisa apresentar um formato válido e não pode ser duplicado. Quando a idade é informada, ela deve ser um número inteiro não negativo.

Em caso de entrada inválida:

```json
{
    "error": "Mensagem descrevendo o problema."
}
```

Status: `400 Bad Request`.

## Persistência

Os dados são armazenados provisoriamente no arquivo `data/usuarios.json`. A geração de IDs utiliza o maior identificador existente e acrescenta 1.

## Códigos HTTP

- `200 OK`: operação realizada com sucesso.
- `201 Created`: usuário criado com sucesso.
- `204 No Content`: usuário removido com sucesso.
- `400 Bad Request`: dados inválidos ou campos obrigatórios ausentes.
- `404 Not Found`: usuário não encontrado.

## Testes

Os endpoints devem ser testados com Postman, Insomnia ou Thunder Client, contemplando cenários de sucesso e falha.

## Autor

Desenvolvido por **Anny Brandão Leite** como atividade acadêmica da disciplina de Desenvolvimento Back-end.
