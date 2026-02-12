from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.base import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)

    action = Column(String, nullable=False)  # e.g. "SUSPEND_USER"
    description = Column(String, nullable=True)

    actor_user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True
    )

    target_user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True
    )

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    actor = relationship(
        "User",
        foreign_keys=[actor_user_id]
    )

    target = relationship(
        "User",
        foreign_keys=[target_user_id]
    )
