from datetime import datetime

def get_stage_and_tone(due_date):

    today = datetime.today()
    due = datetime.strptime(due_date, "%Y-%m-%d")

    overdue_days = (today - due).days

    if overdue_days <= 7:
        return overdue_days, "Warm & Friendly"

    elif overdue_days <= 14:
        return overdue_days, "Polite but Firm"

    elif overdue_days <= 21:
        return overdue_days, "Formal & Serious"

    elif overdue_days <= 30:
        return overdue_days, "Stern & Urgent"

    else:
        return overdue_days, "Escalate to Legal"