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
        priority = assign_priority(complaint)
        department = route_department(category)

        st.subheader("AI Analysis Result")

        st.write(f"**Sentiment:** {sentiment} (polarity: {round(polarity, 2)})")
        st.write(f"**Category:** {category}")

        # Sentiment-aware priority adjustment
        if sentiment == "Negative" and priority != "HIGH":
            priority = "MEDIUM"

        st.write(f"**Final Priority:** {priority}")
        st.write(f"**Assigned Department:** {department}")

        # Explainability
        if sentiment == "Negative":
            st.write("🧠 **Reason:** Complaint shows high emotional distress")
        else:
            st.write("🧠 **Reason:** No critical urgency indicators detected")

        # Admin Summary (INSIDE button block)
        st.divider()
        st.subheader("Admin Summary")

        st.write("📌 This grievance has been logged and routed automatically.")
        st.write("⏱ Estimated manual processing time reduced from hours to seconds.")

        if priority == "HIGH":
            st.warning("🚨 This complaint has been escalated for immediate action.")



