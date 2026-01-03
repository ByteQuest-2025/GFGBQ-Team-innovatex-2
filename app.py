import streamlit as st
from classifier import classify_complaint
from priority import assign_priority
from router import route_department

st.set_page_config(page_title="AI Grievance Redressal")

st.title("AI-Powered Grievance Redressal System")

complaint = st.text_area("Enter your grievance:")

if st.button("Submit Complaint"):
    if complaint.strip() == "":
        st.warning("Please enter a complaint.")
    else:
        category = classify_complaint(complaint)
        priority = assign_priority(complaint)
        department = route_department(category)

        st.subheader("Analysis Result")
        st.write(f"**Category:** {category}")
        st.write(f"**Priority:** {priority}")
        st.write(f"**Assigned Department:** {department}")
