from app.models.user import User
from app.models.hearing import Hearing
from app.models.case import Case


# ============================================================
# WhatsApp Notification (INTEGRATION POINT)
# ============================================================
def send_whatsapp_message(
    *,
    user: User,
    case: Case,
    hearing: Hearing,
) -> bool:
    """
    MVP WhatsApp sender (SIMULATED).

    🔌 REAL API INTEGRATION GOES HERE:
    - Twilio WhatsApp API
    - Meta WhatsApp Business API
    - Any third-party provider
    """

    phone = user.phone

    message = (
        f"📢 Court Reminder\n\n"
        f"Case: {case.title}\n"
        f"Court: {case.court_name}\n"
        f"Date: {hearing.hearing_date}\n"
        f"Time: {hearing.hearing_time}\n"
    )

    # --------------------------------------------------------
    # ❌ CURRENT (MVP)
    # --------------------------------------------------------
    print(f"[WHATSAPP → {phone}] {message}")

    # --------------------------------------------------------
    # ✅ FUTURE (REAL IMPLEMENTATION EXAMPLE)
    # --------------------------------------------------------
    # twilio_client.messages.create(
    #     from_="whatsapp:+14155238886",
    #     to=f"whatsapp:{phone}",
    #     body=message
    # )

    return True  # return False if API fails

# ============================================================
# SMS Notification (INTEGRATION POINT)
# ============================================================
def send_sms_message(
    *,
    user: User,
    case: Case,
    hearing: Hearing,
) -> bool:
    """
    MVP SMS sender (SIMULATED).

    🔌 REAL API INTEGRATION GOES HERE:
    - Twilio SMS
    - Telenor / Jazz / Ufone gateway
    """

    phone = user.phone

    message = (
        f"Court Reminder: {case.title} "
        f"on {hearing.hearing_date} "
        f"at {hearing.hearing_time}"
    )

    # --------------------------------------------------------
    # ❌ CURRENT (MVP)
    # --------------------------------------------------------
    print(f"[SMS → {phone}] {message}")

    # --------------------------------------------------------
    # ✅ FUTURE (REAL IMPLEMENTATION)
    # --------------------------------------------------------
    # sms_provider.send(phone, message)

    return True
