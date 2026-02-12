from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.audit_log import AuditLog
from app.models.user import User
from app.models.case import Case
from app.models.hearing import Hearing
from app.models.document import Document

from app.api.deps import get_db, get_current_admin
from app.models.user import User
from app.schemas.admin import (
    AdminOverviewOut,
    AdminUserInspectionOut,
    AdminUserOut,
    AuditLogOut,
)
from app.services.admin_service import (
    get_admin_overview,
    inspect_user,
    set_user_active_status,
)

router = APIRouter(tags=["Admin"])


@router.get(
    "/overview",
    response_model=AdminOverviewOut
)
def admin_overview(
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin),
):
    """
    Admin dashboard overview:
    - total users
    - total cases
    - total hearings
    - total documents
    """
    return get_admin_overview(db)


@router.get(
    "/users/{user_id}",
    response_model=AdminUserInspectionOut
)
def admin_inspect_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin),
):
    data = inspect_user(db=db, user_id=user_id)

    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return data


@router.post(
    "/users/{user_id}/suspend",
    response_model=AdminUserOut
)
def suspend_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin),
):
    user = set_user_active_status(
        db=db,
        user_id=user_id,
        is_active=False
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user


@router.post(
    "/users/{user_id}/activate",
    response_model=AdminUserOut
)
def activate_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin),
):
    user = set_user_active_status(
        db=db,
        user_id=user_id,
        is_active=True
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user


@router.get(
    "/audit-logs",
    response_model=list[AuditLogOut]
)

def get_audit_logs(
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin),
):
    return (
        db.query(AuditLog)
        .order_by(AuditLog.created_at.desc())
        .limit(100)
        .all()
    )


@router.get("/system-health")
def system_health(
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin),
):
    return {
        "status": "ok",
        "database": "connected",
        "users": db.query(User).count(),
        "cases": db.query(Case).count(),
        "hearings": db.query(Hearing).count(),
        "documents": db.query(Document).count(),
    }


