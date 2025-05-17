# 🚀 FastAPI CRUD API Study



![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)


Projeto simples de estudo com **FastAPI** para criar uma API CRUD (Create, Read, Update, Delete) de itens.

---


## 📚 Recursos

- ✅ Criação de itens com validação de dados via **Pydantic**
- 🔍 Leitura de itens individuais ou todos
- ✏️ Atualização e exclusão de itens
- ⚠️ Tratamento de erros com `HTTPException`


---

## ⚙️ Tecnologias Utilizadas

- [**FastAPI**](https://fastapi.tiangolo.com/)
- [**Pydantic**](https://docs.pydantic.dev/)
- [**Uvicorn**](https://www.uvicorn.org/)

---

## 🛠️ Como Executar
1. Instale as dependências:
```bash
pip install fastapi uvicorn 
```
Execute o servidor:

```
uvicorn main:app --reload
```
📝 Exemplo de Uso
Criar item:

```
curl -X POST "http://localhost:8000/items/1" -H "Content-Type: application/json" -d '{"name":"Livro","description":"Aprendendo FastAPI","price":49.90}'
```
Buscar todos os itens:
```
curl "http://localhost:8000/items/"
```
##  📌 Nota de Estudo

Este projeto faz parte dos meus estudos em:

Criação de APIs com FastAPI

Operações CRUD básicas

Validação de dados com Pydantic

Tratamento de erros HTTP
