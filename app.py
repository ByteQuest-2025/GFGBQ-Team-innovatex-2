import streamlit as st
import pandas as pd
from classifier import classify_complaint
from priority import assign_priority
from router import route_department
from sentiment import analyze_sentiment

st.markdown("""
<style>
/* Main background */
.stApp {
    background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
}

/* Titles */
h1 {
    color: #2C3E50;
}
h2, h3 {
    color: #34495E;
}

/* Section headers */
.section {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

/* Priority badges */
.priority-high {
    color: white;
    background-color: #E74C3C;
    padding: 6px 12px;
    border-radius: 8px;
    font-weight: bold;
}

.priority-medium {
    color: white;
    background-color: #F39C12;
    padding: 6px 12px;
    border-radius: 8px;
    font-weight: bold;
}

.priority-low {
    color: white;
    background-color: #27AE60;
    padding: 6px 12px;
    border-radius: 8px;
    font-weight: bold;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #2C3E50;
}
section[data-testid="stSidebar"] * {
    color: white;
}
</style>
""", unsafe_allow_html=True)


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

        if priority == "HIGH":
            st.markdown('<span class="priority-high">HIGH PRIORITY</span>', unsafe_allow_html=True)
        elif priority == "MEDIUM":
            st.markdown('<span class="priority-medium">MEDIUM PRIORITY</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="priority-low">LOW PRIORITY</span>', unsafe_allow_html=True)

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

# Sidebar Admin Dashboard
st.sidebar.header("🛠 Admin Dashboard")

if st.session_state.complaints:
    df = pd.DataFrame(st.session_state.complaints)

    st.sidebar.metric(
        "Total Complaints",
        len(df)
    )

    high_count = len(df[df["Priority"] == "HIGH"])
    st.sidebar.metric(
        "High Priority",
        high_count
    )

    st.sidebar.subheader("All Complaints")
    st.sidebar.dataframe(df)

else:
    st.sidebar.write("No complaints submitted yet.")

