from app.schemas.category import Category
from fastapi import HTTPException, Depends
from app.db import category_collection

# Get a category by its name
async def get_category_by_name(category_name: str):
    category = await category_collection.find_one({"name": category_name})
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return Category(**category)

# Create a new category
async def create_category(category: Category):
    existing_category = await category_collection.find_one({"name": category.name})
    if existing_category:
        raise HTTPException(status_code=400, detail="Category already exists")
    category_model = category.model_dump()
    result = await category_collection.insert_one(category_model)
    return Category(**category_model)

# Update a category by its name 
async def update_category(category_name: str, category: Category):
    existing_category = await category_collection.find_one({"name": category_name})
    if not existing_category:
        raise HTTPException(status_code=404, detail="Category not found")
    update_category = category.model_dump(exclude_unset=True)
    await category_collection.update_one({"name": category_name}, {"$set": update_category})
    return Category(**{**existing_category, **update_category})

# Delete a category by its name
async def delete_category(category: Category):
    existing_category = await category_collection.find_one({"name": category.name}) 
    if not existing_category:
        raise HTTPException(status_code=404, detail="Category not found")
    await category_collection.delete_one({"name": category.name})
    return Category(**existing_category)