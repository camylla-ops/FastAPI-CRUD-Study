from fastapi import FastAPI, HTTPException
from pydantic import BaseModel



app = FastAPI()

# criar um dicionário para armazenar os itens 
items = {}

# define o modelo de dados para os itens
class Item(BaseModel):
    name: str
    description: str = None
    price: float

#define a rota para criar um item
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item já existe")
    items[item_id] = item
    return {"message": "Item criado com sucesso", "item": item}

# Define a rota para ler um item 
@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return items[item_id]


#define a rota para deletar um item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    del items[item_id]
    return {"message": "Item deletado com sucesso"}   

#define a rota para atualizar um item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    items[item_id] = item
    return {"message": "Item atualizado com sucesso", "item": item}