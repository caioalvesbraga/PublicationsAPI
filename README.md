# FastAPI Publication API

## Sobre
Esta API permite gerenciar publicações, incluindo operações de CRUD (Create, Read, Update, Delete) em um banco de dados SQLite.
A arquitetura segue os princípios do **Clean Architecture**, **SOLID** e **Clean Code**, garantindo um código modular e bem estruturado.

## Tecnologias Utilizadas
- **FastAPI**: Framework para criação de APIs rápidas e eficientes.
- **SQLite**: Banco de dados leve e fácil de configurar.
- **SQLAlchemy**: ORM para manipulação do banco de dados.
- **Pydantic**: Validação e tipagem de dados.
- **Uvicorn**: Servidor ASGI para rodar a aplicação.

## Pré-requisitos
Antes de rodar a aplicação, certifique-se de ter o **Python 3.10+** instalado.

## Como Executar

### 1. Crie um Ambiente Virtual e Instale as Dependências
```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows

pip install -r requirements.txt
```

### 2. Execute a Aplicação
```sh
uvicorn main:app --reload
```
A API estará disponível em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Uso da API

### 1. Acesse a Documentação Interativa
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### 2. Endpoints Principais

#### Criar uma Publicação
**POST** `/publications/`
```json
{
  "titulo": "Clean Code",
  "autor": "Robert C. Martin",
  "isbn": 123456789,
  "paginas": 464,
  "ano": 2008
}
```

#### Listar Publicações
**GET** `/publications/`

#### Buscar uma Publicação por ID
**GET** `/publications/{id}`

#### Atualizar uma Publicação
**PUT** `/publications/{id}`

#### Deletar uma Publicação
**DELETE** `/publications/{id}`

## Estrutura do Projeto
```
📂 publications_api
├── 📂 routers
│   ├── publication_router.py
├── 📂 services
│   ├── publication_service.py
├── 📂 repositories
│   ├── publication_repository.py
├── 📂 models
│   ├── publication.py
├── 📂 schemas
│   ├── publication_schema.py
├── main.py
├── database.py
├── requirements.txt
├── README.md
```

## Tratamento de Erros
A API inclui tratamento semântico de erros, retornando mensagens específicas para casos como:
- Publicação não encontrada (`404 Not Found`)
- Dados inválidos (`422 Unprocessable Entity`)
- Publicação duplicada (`400 Bad Request`)

---

