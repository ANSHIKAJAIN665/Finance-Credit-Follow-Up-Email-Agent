```text
# Finance Credit Follow-Up Email Agent

## Project Overview

The Finance Credit Follow-Up Email Agent is an AI-powered prototype developed to automate overdue invoice reminder workflows for finance teams.

The system reads invoice records from a CSV file, determines overdue stages, generates personalized follow-up emails with different escalation tones, and maintains audit logs for tracking.

This project was developed as part of the AI Enablement Internship Task 2.

---

# Features

- Invoice data ingestion using CSV
- Automatic overdue day calculation
- Tone escalation engine
- Personalized follow-up email generation
- Legal escalation detection
- Dry-run email simulation
- Audit logging system
- Streamlit-based dashboard UI

---

# Tone Escalation Logic

| Overdue Days | Tone |
|---|---|
| 1–7 Days | Warm & Friendly |
| 8–14 Days | Polite but Firm |
| 15–21 Days | Formal & Serious |
| 22–30 Days | Stern & Urgent |
| 30+ Days | Escalate to Legal |

---

# Project Architecture

CSV Invoice Data
        ↓
Pandas Data Processing
        ↓
Overdue & Escalation Logic
        ↓
Email Generation Engine
        ↓
Audit Logging
        ↓
Streamlit Dashboard

---

# Folder Structure

Finance_email_agent/

│
├── app.py
├── requirements.txt
├── README.md
├── .env

│
├── data/
│   └── invoices.csv

│
├── logs/
│   └── email_logs.json

│
└── utils/
    ├── escalation.py
    ├── generator.py
    └── logger.py

---

# Technologies Used

| Component | Technology |
|---|---|
| Programming Language | Python |
| UI Framework | Streamlit |
| Data Handling | Pandas |
| Logging | JSON |
| Environment Variables | python-dotenv |

---

# Setup Instructions

## 1. Clone Repository

git clone <repository-link>

cd Finance_email_agent

---

## 2. Create Virtual Environment

Windows:

python -m venv venv

venv\Scripts\activate

---

## 3. Install Dependencies

pip install -r requirements.txt

---

## 4. Run Streamlit App

streamlit run app.py

---

# Sample Workflow

1. User loads invoice CSV data
2. System calculates overdue days
3. Appropriate escalation tone is selected
4. Personalized follow-up email is generated
5. Email logs are stored in audit logs
6. Legal escalation cases are flagged

---

# Security Mitigations

## Prompt Injection Protection
- Structured template-based generation
- Controlled invoice input fields

## API Key Protection
- API keys stored in `.env`
- No hardcoded credentials

## Data Privacy
- Local CSV processing
- No external database storage

## Hallucination Reduction
- Data-driven email generation
- Fixed escalation templates

## Unauthorized Access
- Local execution environment
- No public API endpoints exposed

## Email Safety
- Dry-run mode enabled
- No real client emails sent

---

# Future Improvements

- Real SMTP integration
- AI-generated dynamic email content
- Dashboard analytics
- Database integration
- Role-based authentication
- Multi-language support

---

# Demo Output

The application successfully:
- Generates personalized finance follow-up emails
- Applies escalation logic automatically
- Flags legal escalation cases
- Stores audit logs for review

---

# Author

Anshika Jain
```
