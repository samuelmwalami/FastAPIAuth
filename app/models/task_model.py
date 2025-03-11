from pydantic import BaseModel, Field
import uuid

class Task(BaseModel):
    id: uuid.UUID = Field(default_factory= uuid.uuid4)
    name: str
    model_config = {"extra" : "forbid"}