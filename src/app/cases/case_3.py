"""
Case: Field
"""
from fastapi import APIRouter
from pydantic import BaseModel, Field, PositiveInt

router = APIRouter(prefix="/case-3")


class Model(BaseModel):
    integer: PositiveInt
    gt_integer: int = Field(..., gt=0)
    ge_integer: int = Field(..., ge=1)


@router.get("/{integer}")
def get_model(integer: PositiveInt):
    return Model(integer=integer, gt_integer=integer, ge_integer=integer)
