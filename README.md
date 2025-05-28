# 🚀 FastAPI CRUD - Projeto de Estudo

![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)

Este é um projeto simples de API CRUD (Create, Read, Update, Delete) desenvolvido com [FastAPI](https://fastapi.tiangolo.com/) para fins de aprendizado. Ele permite criar, consultar, atualizar e deletar itens em memória, com validação de dados usando Pydantic.

---

## ✨ Funcionalidades

- **Criar** itens com validação automática de dados
- **Consultar** um item específico ou todos os itens
- **Atualizar** itens existentes
- **Deletar** itens
- **Tratamento de erros** com respostas HTTP apropriadas

---

## 🛠️ Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/) (servidor ASGI)

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd <nome-da-pasta>
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install fastapi uvicorn
   ```

4. **Execute o servidor:**
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Acesse a documentação interativa:**
   - [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📦 Exemplos de Uso

### Criar um item
```bash
curl -X POST "http://localhost:8000/items/1" -H "Content-Type: application/json" -d '{"name":"Livro","description":"Aprendendo FastAPI","price":49.90}'
```

### Buscar todos os itens
```bash
curl "http://localhost:8000/items"
```

### Buscar um item específico
```bash
curl "http://localhost:8000/items/1"
```

### Atualizar um item
```bash
curl -X PUT "http://localhost:8000/items/1" -H "Content-Type: application/json" -d '{"name":"Livro Atualizado","description":"Nova descrição","price":59.90}'
```

### Deletar um item
```bash
curl -X DELETE "http://localhost:8000/items/1"
```

---

## 📚 Sobre

Este projeto foi criado para fins de estudo, visando praticar:

- Criação de APIs REST com FastAPI
- Operações CRUD básicas
- Validação de dados com Pydantic
- Tratamento de erros HTTP

---

Sinta-se à vontade para usar, modificar e compartilhar!
