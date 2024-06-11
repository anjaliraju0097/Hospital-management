# schemas.py
from ninja import Schema
from typing import Optional

class RolesSchema(Schema):
    id: Optional[int]
    title: str
    status: bool
   
