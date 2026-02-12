from datetime import datetime
from sqlalchemy.orm import Session

from app.models.reminder import Reminder
from app.services.notification_service import (
    send_whatsapp_message,
    send_sms_message,
)


def process_due_reminders(db: Session) -> int:
    """
    Process reminders that:
    - are not sent
    - remind_at <= current time (UTC)

    Flow:
    1️⃣ Find due reminders
    2️⃣ Send WhatsApp (primary)
    3️⃣ Fallback to SMS (if WhatsApp fails)
    4️⃣ Mark reminder as sent
    """

    now = datetime.utcnow()

    reminders = (
        db.query(Reminder)
        .filter(
            Reminder.is_sent.is_(False),
            Reminder.remind_at <= now
        )
        .order_by(Reminder.remind_at)
        .all()
    )

    processed_count = 0

    for reminder in reminders:
        hearing = reminder.hearing
        case = hearing.case if hearing else None
        user = reminder.user

        # -------------------------
        # Safety checks
        # -------------------------
        if not hearing or not case or not user:
            reminder.is_sent = True
            reminder.sent_at = now
            continue

        # -------------------------
        # Send WhatsApp (Primary)
        # -------------------------
        whatsapp_sent = send_whatsapp_message(
            user=user,
            case=case,
            hearing=hearing
        )

        # -------------------------
        # SMS fallback (Secondary)
        # -------------------------
        if not whatsapp_sent:
            send_sms_message(
                user=user,
                case=case,
                hearing=hearing
            )

        # -------------------------
        # Mark reminder as sent
        # -------------------------
        reminder.is_sent = True
        reminder.sent_at = now
        processed_count += 1

    db.commit()
    return processed_count
