from typing import Optional

from models.category import Category
from pydantic import BaseModel, StrictInt, StrictStr, ConfigDict

from models.tag import Tag


class Pet(BaseModel):
    model_config = ConfigDict(extra='forbid')

    id: StrictInt
    category: Optional[Category] = None
    name: Optional[StrictStr] = None
    photoUrls: list[str]
    tags: list[Tag]
    status: Optional[StrictStr] = None


statuses = ('available', 'pending', 'sold')