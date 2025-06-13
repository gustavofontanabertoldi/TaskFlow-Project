from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import date

class TaskBase(BaseModel):
    title: str 
    description: Optional[str] 
    due_date: Optional[date] = None
    status: Literal['pending', 'in_progress', 'completed'] = 'pending'  
    category_id: Optional[str] = None