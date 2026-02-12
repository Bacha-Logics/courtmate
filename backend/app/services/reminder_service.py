from datetime import datetime, timedelta, time
from sqlalchemy.orm import Session

from app.models.reminder import Reminder
from app.models.hearing import Hearing
from app.models.user import User


def create_reminders_for_hearing(
    *,
    db: Session,
    hearing: Hearing,
    current_user: User,
):
    """
    Create automatic reminders for a hearing:
    - 1 day before
    - 2 hours before (only if hearing_time exists)
    """

    reminders = []
    now = datetime.utcnow()

    # -------------------------
    # 1️⃣ Reminder: 1 day before
    # -------------------------
    reminder_time = hearing.hearing_time or time(0, 0)

    remind_at_day_before = datetime.combine(
        hearing.hearing_date,
        reminder_time
    ) - timedelta(days=1)

    if remind_at_day_before > now:
        reminders.append(
            Reminder(
                remind_at=remind_at_day_before,
                hearing_id=hearing.id,
                user_id=current_user.id,
                is_sent=False,
            )
        )

    # -------------------------
    # 2️⃣ Reminder: 2 hours before (only if time exists)
    # -------------------------
    if hearing.hearing_time:
        hearing_datetime = datetime.combine(
            hearing.hearing_date,
            hearing.hearing_time
        )
        remind_at_2_hours = hearing_datetime - timedelta(hours=2)

        if remind_at_2_hours > now:
            reminders.append(
                Reminder(
                    remind_at=remind_at_2_hours,
                    hearing_id=hearing.id,
                    user_id=current_user.id,
                    is_sent=False,
                )
            )

    db.add_all(reminders)
    db.commit()

    return reminders
