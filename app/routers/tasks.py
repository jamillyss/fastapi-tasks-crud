from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlmodel import Session, select
from ..database import get_session
from ..models import Task, TaskCreate, TaskRead, TaskUpdate
from datetime import datetime

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate, session: Session = Depends(get_session)):
    task = Task(**payload.dict())
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@router.get("/", response_model=List[TaskRead])
def list_tasks(
    session: Session = Depends(get_session),
    skip: int = 0,
    limit: int = Query(50, le=100),
    done: Optional[bool] = None,
):
    stmt = select(Task)
    if done is not None:
        stmt = stmt.where(Task.done == done)
    stmt = stmt.offset(skip).limit(limit)
    tasks = session.exec(stmt).all()
    return tasks

@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskRead)
@router.patch("/{task_id}", response_model=TaskRead)
def update_task(task_id: int, payload: TaskUpdate, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    changed = False
    for field, value in payload.dict(exclude_unset=True).items():
        setattr(task, field, value)
        changed = True

    if changed:
        task.updated_at = datetime.utcnow()
        session.add(task)
        session.commit()
        session.refresh(task)
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    session.delete(task)
    session.commit()
    return None
