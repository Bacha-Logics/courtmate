from sqlalchemy import Column, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base import Base


class Reminder(Base):
    __tablename__ = "reminders"

    id = Column(Integer, primary_key=True, index=True)

    # When reminder should fire
    remind_at = Column(DateTime, nullable=False)

    # Whether reminder is already sent
    is_sent = Column(Boolean, default=False)

    # Foreign keys
    hearing_id = Column(Integer, ForeignKey("hearings.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    # 🔗 Relationships (THIS is where your code goes)
    hearing = relationship("Hearing", back_populates="reminders")
    user = relationship("User")
