# schemas.py
from ninja import Schema
from typing import Optional

class UserSchema(Schema):
    id: Optional[int]
    name: str
    email: str
    role_id: Optional[int]
    # phone

