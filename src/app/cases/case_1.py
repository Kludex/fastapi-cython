"""
Case: Simple model
"""
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/case-1")


class Model(BaseModel):
    integer: int
    string: str


@router.get("/{integer}")
def get_model(integer: int):
    return Model(integer=integer, string="string")
