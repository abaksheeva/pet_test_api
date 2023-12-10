from pydantic import BaseModel, StrictInt


class Category(BaseModel):
    id: StrictInt
    name: str
