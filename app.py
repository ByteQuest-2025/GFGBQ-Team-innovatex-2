import streamlit as st
import pandas as pd
from classifier import classify_complaint
from priority import assign_priority
from router import route_department
from sentiment import analyze_sentiment

st.set_page_config(page_title="AI Grievance Redressal")

st.title("AI-Powered Grievance Redressal System")

# Store complaints for admin dashboard
if "complaints" not in st.session_state:
    st.session_state.complaints = []

st.header("Citizen Complaint Portal")

complaint = st.text_area("Enter your grievance:")

if st.button("Submit Complaint"):

    if complaint.strip() == "":
        st.warning("Please enter a complaint.")

    else:
        st.divider()
        st.header("AI Analysis & Routing")

        # NLP analysis
        sentiment, polarity = analyze_sentiment(complaint)
        category = classify_complaint(complaint)
        priority, score, reasons = assign_priority(complaint)
        department = route_department(category)

        st.subheader("AI Analysis Result")

        st.write(f"**Sentiment:** {sentiment} (polarity: {round(polarity, 2)})")
        st.write(f"**Category:** {category}")

        # Sentiment as supporting signal
        if sentiment == "Negative" and priority == "LOW":
            priority = "MEDIUM"
            score = max(score, 40)

        st.write(f"**Final Priority:** {priority}")
        st.write(f"**Priority Score:** {score}/100")

        if reasons:
            st.write("🧠 **Reason(s):**")
            for r in reasons:
                st.write(f"- {r}")

        st.write(f"**Assigned Department:** {department}")

        # Sentiment insight
        if sentiment == "Negative":
            st.write("🧠 **Sentiment Insight:** High emotional distress detected")
        else:
            st.write("🧠 **Sentiment Insight:** Complaint tone is neutral")

        # Admin summary
        st.divider()
        st.subheader("Admin Summary")

        st.write("📌 This grievance has been logged and routed automatically.")
        st.write("⏱ Estimated manual processing time reduced from hours to seconds.")

        if priority == "HIGH":
            st.warning("🚨 This complaint has been escalated for immediate action.")

        # Save complaint for dashboard
        st.session_state.complaints.append({
            "Complaint": complaint,
            "Category": category,
            "Priority": priority,
            "Score": score,
            "Department": department
        })

# Admin Dashboard
st.divider()
st.header("Admin Dashboard")

if st.session_state.complaints:
    df = pd.DataFrame(st.session_state.complaints)
    st.dataframe(df)
else:
    st.write("No complaints submitted yet.")
