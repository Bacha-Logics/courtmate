from pydantic import BaseModel
from datetime import date, time
from typing import Optional


# -------------------------
# Shared fields
# -------------------------
class HearingBase(BaseModel):
    hearing_date: Optional[date] = None
    hearing_time: Optional[time] = None
    notes: Optional[str] = None


# -------------------------
# Create hearing
# -------------------------
class HearingCreate(HearingBase):
    case_id: int
    hearing_date: date   # ✅ REQUIRED on create


# -------------------------
# Response schema
# -------------------------
class HearingOut(HearingBase):
    id: int
    case_id: int
    hearing_date: date   # ✅ ALWAYS present in response

    class Config:
        from_attributes = True
