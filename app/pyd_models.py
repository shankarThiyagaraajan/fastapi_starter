# ** Base Modules
from datetime import datetime
# ** External Modules
from pydantic import BaseModel


class UserBase(BaseModel):
    fname: str
    lname: str
    email: str
    password: str
    is_active: bool = True
    created_at: datetime
    updated_at: datetime

# ---------------------------- OAuth --------------------------


class Token(BaseModel):
    access_token: str
    token_type: str
# ---------------------------- OAuth: END --------------------------
