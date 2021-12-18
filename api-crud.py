from enum import unique
from typing_extensions import Required
from pydantic import BaseModel, Field
from fastapi import FastAPI
from fastapi_crudrouter import MemoryCRUDRouter
from pydantic.errors import DateTimeError
import uvicorn
from datetime import datetime


class Product(BaseModel):
    pruductid: int
    title: str
    sku: str
    barcodes: str
    description: str
    price: float
    created: datetime = Field(default_factory=datetime.utcnow)

app = FastAPI()
router = MemoryCRUDRouter(schema=Product)
app.include_router(router)

uvicorn.run(app, host='0.0.0.0', port=5000, workers=1)