# ✅ FastAPI Tasks CRUD

API simples de **tarefas (To-Do List)** feita com **FastAPI + SQLModel + Pytest**.  
📌 Projeto de estudo para praticar **APIs**, **banco de dados SQLite** e **testes automatizados**.

---

## 🚀 Como rodar

```bash
# 1. Clonar o repositório
git clone https://github.com/SEU-USUARIO/fastapi-tasks-crud.git
cd fastapi-tasks-crud

# 2. Criar ambiente virtual (Windows PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Rodar servidor
python -m uvicorn app.main:app --reload


---


# 🔗 Links:

API: http://127.0.0.1:8000

Documentação Swagger: http://127.0.0.1:8000/docs


---


# 🧪 Rodar os testes
pytest -q


---


# 📋 Resultado esperado:
.....    [100%]
5 passed in X.XXs


---


# 📚 Endpoints principais

POST /tasks/ → cria tarefa

GET /tasks/ → lista tarefas (filtro por done=true/false)

GET /tasks/{id} → busca tarefa pelo ID

PATCH /tasks/{id} → atualiza parcialmente

DELETE /tasks/{id} → exclui tarefa


---


# 📝 Notas

Banco de dados: SQLite (tasks.db) criado automaticamente.

Testes cobrem: criação, leitura, atualização, exclusão e erro 404.

Projeto pensado para aprender e demonstrar QA com Pytest.

Ideal para quem está iniciando em QA + desenvolvimento e quer um projeto rápido no portfólio.