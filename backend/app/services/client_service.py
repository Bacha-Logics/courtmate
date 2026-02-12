from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.case import Case
from app.models.user import User


def get_clients(db: Session, current_user: User):
    """
    Returns distinct clients derived from cases
    """

    rows = (
        db.query(
            Case.client_name,
            Case.client_phone,
            func.count(Case.id).label("total_cases")
        )
        .filter(
            Case.user_id == current_user.id,
            Case.client_phone.isnot(None)
        )
        .group_by(Case.client_name, Case.client_phone)
        .order_by(func.count(Case.id).desc())
        .all()
    )

    return [
        {
            "client_name": r.client_name,
            "client_phone": r.client_phone,
            "total_cases": r.total_cases
        }
        for r in rows
    ]


def get_client_cases(
    db: Session,
    current_user: User,
    client_phone: str
):
    return (
        db.query(Case)
        .filter(
            Case.user_id == current_user.id,
            Case.client_phone == client_phone
        )
        .all()
    )
