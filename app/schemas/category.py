from pydantic import BaseModel, Field
from typing import Optional

class CategoryBase(BaseModel):
    name: str = Field(..., example="Faculdade")
    color: Optional[str] = Field(None, example="#FF0000")

class Category(CategoryBase):
    id: str = Field(..., alilas="_id")
    class Config:
        Allow_population_by_field_name = True