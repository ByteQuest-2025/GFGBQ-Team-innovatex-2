# AI for Grievance Redressal in Public Governance

An AI-powered prototype that automatically analyzes citizen grievances, prioritizes them based on urgency and sentiment, and routes them to the appropriate government department for faster resolution.

---

## Problem Statement
Public governance bodies receive thousands of unstructured citizen complaints daily.  
Manual review causes delays, backlogs, and lack of prioritization, leading to poor citizen satisfaction.

---

## Our Solution
We designed an AI-driven grievance redressal system that:
- Understands free-text citizen complaints
- Classifies grievances into relevant categories
- Assigns priority based on urgency and sentiment
- Routes complaints to the correct department automatically
- Provides explainable decisions for transparency

---

## Key Features
- Rule-based NLP for grievance classification
- Sentiment analysis to capture emotional urgency
- Priority-based grievance handling (High / Medium / Low)
- Automatic department routing
- Explainable AI outputs
- Admin summary for governance impact

---

## Technology Stack
- Python
- Streamlit (UI)
- TextBlob (Sentiment Analysis)
- Rule-based NLP logic

---

## Why This Approach
For public governance systems, transparency and explainability are critical.  
Rule-based NLP combined with sentiment analysis ensures fast, reliable, and auditable decision-making.

---

## Impact & Practicality
- Reduces manual grievance processing time from hours to seconds
- Ensures urgent public safety issues are prioritized
- Scalable for large volumes of citizen complaints
- Suitable for real-world governance deployment

---

## Future Scope
- Integration with NLP APIs for multilingual complaints
- Machine learning models for advanced semantic understanding
- Real-time dashboards for authorities
- Citizen notifications via SMS / Email

---

## How to Run the Project
```bash
pip install -r requirements.txt
streamlit run app.py

