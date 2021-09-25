"""
Case 2: Optional on schema
"""
from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/case-2")


class Model(BaseModel):
    integer: int
    string: str
    int_optional: int = None
    str_optional: Optional[str] = None


@router.get("/{integer}", response_model=Model, response_model_exclude_none=True)
def get_model(
    integer: int, int_optional: int = None, str_optional: Optional[str] = None
):
    return {
        "integer": integer,
        "string": "string",
        "int_optional": int_optional,
        "str_optional": str_optional,
    }
