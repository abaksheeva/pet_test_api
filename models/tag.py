from pydantic import BaseModel, StrictInt, StrictStr


class Tag(BaseModel):
    id: StrictInt
    name: StrictStr
