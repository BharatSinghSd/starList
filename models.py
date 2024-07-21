from pydantic import BaseModel

class StarInDB(BaseModel):
    id: str
    starName: str
