from app.schemas.task import TaskBase
from fastapi import HTTPException, Depends
from app.db import task_collection

# Get a tasks by the name
async def get_task_by_name(task_name: str):
    task = await task_collection.find_one({"title": task_name})
    if not task:
        raise HTTPException(status_code=404, detail="task not found")
    return TaskBase(**task)

# Create a new task
async def create_task(task: TaskBase):
    existing_task = await task_collection.find_one({"title": task.title})
    if existing_task:
        raise HTTPException(status_code=400, detail="task already exists")
    task_model = task.model_dump()
    result = await task_collection.insert_one(task_model)
    return TaskBase(**task_model)

# Update a task by its title
async def update_task(task_name: str, task: TaskBase):
    existing_task = await task_collection.find_one({"title": task_name})
    if not existing_task:
        raise HTTPException(status_code=404, detail="task not found")
    
    updated_task = task.model_dump(exclude_unset=True)
    await task_collection.update_one({"title": task_name}, {"$set": updated_task})
    return TaskBase(**{**existing_task, **updated_task})

# Delete a task by its title
async def delete_task(task: TaskBase):
    existing_task = await task_collection.find_one({"title": task.title})
    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")
    await task_collection.delete_one({"title": task.title})
    return TaskBase(**existing_task)