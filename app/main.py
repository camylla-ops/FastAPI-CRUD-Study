from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException
from typing import Dict

app = FastAPI()

# Create a dictionary to store items    
items = {}

# Define a Pydantic model for the item
# This will help with data validation and serialization
class Item(BaseModel):
    name: str
    description: str = None
    price: float

# Define a route to create an item
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item já existe")
    items[item_id] = item
    return {"message": "Item criado com sucesso", "item": item}

# Define a route to read an item
@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return items[item_id]
    
#define a route to delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    del items[item_id]
    return {"message": "Item deletado com sucesso"}   

#define a route to read all items
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    items[item_id] = item
    return {"message": "Item atualizado com sucesso", "item": item}
