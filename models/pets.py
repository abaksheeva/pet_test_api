from pydantic import RootModel

from models.pet import Pet


class Pets(RootModel):
    root: list[Pet]
