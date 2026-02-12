from pydantic import BaseModel
from typing import Optional
from enum import Enum


# -------------------------
# Case Status Enum (API)
# -------------------------
class CaseStatusEnum(str, Enum):
    pending = "pending"
    active = "active"
    closed = "closed"


class CaseBase(BaseModel):
    title: str
    case_number: Optional[str] = None
    court_type: Optional[str] = None
    court_name: Optional[str] = None
    judge_name: Optional[str] = None
    client_name: Optional[str] = None
    client_phone: Optional[str] = None
    opponent_name: Optional[str] = None


class CaseCreate(CaseBase):
    pass  # 🔒 status NOT allowed on create


class CaseUpdate(BaseModel):
    title: Optional[str] = None
    case_number: Optional[str] = None
    court_type: Optional[str] = None
    court_name: Optional[str] = None
    judge_name: Optional[str] = None
    client_name: Optional[str] = None
    client_phone: Optional[str] = None
    opponent_name: Optional[str] = None
    status: Optional[CaseStatusEnum] = None  # allowed ONLY on update


class CaseOut(CaseBase):
    id: int
    user_id: int
    status: CaseStatusEnum

    class Config:
        from_attributes = True
