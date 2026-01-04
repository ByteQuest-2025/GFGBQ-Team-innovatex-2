import streamlit as st
from classifier import classify_complaint
from priority import assign_priority
from router import route_department
from sentiment import analyze_sentiment

st.set_page_config(page_title="AI Grievance Redressal")

st.title("AI-Powered Grievance Redressal System")

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

        # Explainability
        if sentiment == "Negative":
            st.write("🧠 **Reason:** Complaint shows high emotional distress")
        else:
            st.write("🧠 **Sentiment Insight:** Complaint tone is neutral")

        # Admin Summary (INSIDE button block)
        st.divider()
        st.subheader("Admin Summary")

        st.write("📌 This grievance has been logged and routed automatically.")
        st.write("⏱ Estimated manual processing time reduced from hours to seconds.")

        if priority == "HIGH":
            st.warning("🚨 This complaint has been escalated for immediate action.")



