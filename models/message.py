from pydantic import BaseModel, StrictInt, StrictStr, ConfigDict


class Message(BaseModel):
    model_config = ConfigDict(extra='forbid')

    code: StrictInt
    type: StrictStr
    message: StrictStr
