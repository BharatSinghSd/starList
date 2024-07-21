from pydantic import BaseModel

class StarCreate(BaseModel):
    starName: str

class StarUpdate(BaseModel):
    starName: str
