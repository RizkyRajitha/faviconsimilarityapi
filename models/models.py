from pydantic import BaseModel


class ImageQuery(BaseModel):
    name:str
