def generate_email(client, invoice, amount, overdue_days, tone):

    if tone == "Warm & Friendly":

        return f"""
Subject: Friendly Reminder – Invoice {invoice}

Hi {client},

I hope you're doing well.

This is a friendly reminder that invoice {invoice} for ₹{amount} is overdue by {overdue_days} days.

If payment has already been processed, please ignore this email.

Otherwise, kindly complete the payment at your earliest convenience.

Regards,
Finance Team
"""

    elif tone == "Polite but Firm":

        return f"""
Subject: Payment Pending – Invoice {invoice}

Dear {client},

Our records indicate that invoice {invoice} for ₹{amount} remains unpaid and is now overdue by {overdue_days} days.

Please confirm the expected payment date.

Regards,
Finance Team
"""

    elif tone == "Formal & Serious":

        return f"""
Subject: Important: Outstanding Payment – Invoice {invoice}

Dear {client},

Despite previous reminders, invoice {invoice} amounting to ₹{amount} remains unpaid.

The payment is now overdue by {overdue_days} days.

We request immediate attention and a response within 48 hours.

Regards,
Finance Team
"""

    elif tone == "Stern & Urgent":

        return f"""
Subject: FINAL NOTICE – Invoice {invoice}

Dear {client},

This is the final reminder regarding invoice {invoice} for ₹{amount}.

The payment is overdue by {overdue_days} days.

Failure to respond immediately may result in escalation to the legal/recovery team.

Regards,
Finance Team
"""