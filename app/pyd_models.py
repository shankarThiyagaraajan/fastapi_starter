# ** Base Modules
from datetime import datetime
# ** External Modules
from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    is_active: bool = True
    created_at: datetime