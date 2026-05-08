import streamlit as st
import pandas as pd
import json
import os

from utils.escalation import get_stage_and_tone
from utils.generator import generate_email
from utils.logger import save_log

st.set_page_config(
    page_title="Finance Email Agent",
    page_icon="📧",
    layout="wide"
)

st.title("📧 Finance Credit Follow-Up Email Agent")

st.markdown("AI-powered invoice reminder and escalation system")

# Load CSV
df = pd.read_csv("data/invoices.csv")

st.subheader("Invoice Records")
st.dataframe(df, use_container_width=True)

# Generate Emails
if st.button("Generate Emails"):

    st.subheader("Generated Follow-Up Emails")

    for _, row in df.iterrows():

        overdue_days, tone = get_stage_and_tone(row["due_date"])

        # Legal escalation
        if tone == "Escalate to Legal":

            st.warning(
                f"⚠️ {row['client_name']} has crossed 30+ overdue days. Manual finance/legal review required."
            )

            continue

        # Generate Email
        email = generate_email(
            row["client_name"],
            row["invoice_no"],
            row["amount"],
            overdue_days,
            tone
        )

        # Show Tone
        st.markdown(f"## {row['client_name']} — {tone}")

        # Success Message
        st.success(f"Email generated successfully for {row['client_name']}")

        # Email Box
        st.text_area(
            f"Generated Email - {row['invoice_no']}",
            email,
            height=250
        )

        # Save Logs
        save_log({
            "client": row["client_name"],
            "invoice": row["invoice_no"],
            "tone": tone,
            "status": "Dry Run"
        })

# Audit Logs
st.subheader("📜 Audit Logs")

log_path = "logs/email_logs.json"

if os.path.exists(log_path):

    with open(log_path, "r") as f:
        logs = f.readlines()

    for log in logs[-10:]:
        st.code(log)

else:
    st.info("No logs available yet.")