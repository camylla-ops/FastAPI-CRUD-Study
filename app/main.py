from fastapi import FastAPI  # Importa o FastAPI pra criar a aplicação
from pydantic import BaseModel  # Importa o BaseModel pra validar os dados
from fastapi import HTTPException  # Pra lançar erros como 404 ou 400


app = FastAPI()  # Cria a instância da aplicação (a "app" que vai responder às requisições)

# Banco de dados falso: dicionário pra guardar os itens temporariamente
items = {}

# Modelo que define como os dados dos itens devem ser
# Serve pra garantir que os dados enviados são válidos
class Item(BaseModel):
    name: str  # Nome do item (obrigatório)
    description: str = None  # Descrição (opcional)
    price: float  # Preço do item (obrigatório)

# Rota pra criar um item novo
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in items:  # Se o ID já existir, erro 400
        raise HTTPException(status_code=400, detail="Item já existe")
    items[item_id] = item  # Salva o item no dicionário
    return {"message": "Item criado com sucesso", "item": item}

# Rota pra ler um item específico pelo ID
@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:  # Se o item não existir, erro 404
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return items[item_id]  # Retorna o item encontrado

# Rota pra atualizar um item existente
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    items[item_id] = item  # Substitui o item antigo pelo novo
    return {"message": "Item atualizado com sucesso", "item": item}

# Rota pra deletar um item pelo ID
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    del items[item_id]  # Remove o item do dicionário
    return {"message": "Item deletado com sucesso"}

# Rota pra listar todos os itens
@app.get("/items")
def read_all_items():
    return items  # Retorna todos os itens cadastrados
