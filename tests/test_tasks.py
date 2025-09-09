from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_ok():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json().get("ok") is True

def test_create_task_and_get():
    payload = {"title": "Estudar QA", "description": "Pytest + Cypress", "done": False}
    r = client.post("/tasks/", json=payload)
    assert r.status_code == 201
    created = r.json()
    assert created["title"] == payload["title"]
    task_id = created["id"]

    r = client.get(f"/tasks/{task_id}")
    assert r.status_code == 200
    fetched = r.json()
    assert fetched["id"] == task_id

def test_list_tasks_and_filter():
    client.post("/tasks/", json={"title": "Feito", "done": True})
    client.post("/tasks/", json={"title": "Pendente", "done": False})

    r = client.get("/tasks/?done=true")
    assert r.status_code == 200
    items = r.json()
    assert all(item["done"] is True for item in items)

def test_update_task():
    r = client.post("/tasks/", json={"title": "Atualizar", "description": "v1"})
    task = r.json()
    tid = task["id"]

    r = client.patch(f"/tasks/{tid}", json={"description": "v2", "done": True})
    assert r.status_code == 200
    updated = r.json()
    assert updated["description"] == "v2"
    assert updated["done"] is True

def test_delete_task():
    r = client.post("/tasks/", json={"title": "Excluir"})
    tid = r.json()["id"]

    r = client.delete(f"/tasks/{tid}")
    assert r.status_code == 204

    r = client.get(f"/tasks/{tid}")
    assert r.status_code == 404
