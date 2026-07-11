Title: Getting Started with FastAPI: A Modern Python Web Framework
Date: 2025-12-15 10:20
Category: Python
Tags: fastapi, python, web, tutorial
Slug: getting-started-with-fastapi
Cover: images/fastapi-cover.jpg

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Why FastAPI?

FastAPI has gained tremendous popularity since its release, and for good reasons:

- **Performance**: On par with Node.js and Go (thanks to Starlette and Pydantic)
- **Fast to code**: 200% to 300% faster development speed
- **Fewer bugs**: 40% fewer human-induced errors
- **Intuitive**: Great editor support with auto-completion everywhere
- **Easy**: Designed to be easy to use and learn
- **Robust**: Production-ready with automatic interactive documentation
- **Standards-based**: Based on OpenAPI and JSON Schema

## Installation

```bash
pip install fastapi uvicorn
```

## A Simple Example

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

Run it with:

```bash
uvicorn main:app --reload
```

Visit `http://localhost:8000/docs` to see the automatic interactive API documentation.

## Path Operations

FastAPI uses decorators to define path operations:

```python
@app.get("/items/")
@app.post("/items/")
@app.put("/items/{item_id}")
@app.delete("/items/{item_id}")
```

## Request Body with Pydantic

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}
```

## Dependency Injection

FastAPI has a powerful dependency injection system:

```python
from fastapi import Depends

def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items/")
def read_items(commons: dict = Depends(common_parameters)):
    return commons
```

## Conclusion

FastAPI is an excellent choice for building modern web APIs with Python. Its combination of performance, developer experience, and production-ready features makes it one of the best frameworks available today.
