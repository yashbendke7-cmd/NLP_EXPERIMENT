import streamlit as st
from notice_analyzer import analyze_notice

st.set_page_config(page_title="AI College Notice Analyzer", page_icon="🎓")

st.title("🎓 AI College Notice Analyzer")
st.write("Paste a college notice below and the system will extract its category, deadline, time, priority, summary, and keywords.")

notice = st.text_area(
    "Paste College Notice",
    height=250,
    placeholder="Example: TCS campus placement registration is open for eligible students. Last date is 15 September 2026 at 5:00 PM."
)

if st.button("🔍 Analyze Notice"):
    if not notice.strip():
        st.warning("Please enter a notice first.")
    else:
        result = analyze_notice(notice)

        st.subheader("📊 Analysis Result")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Category", result["category"])
            st.metric("Priority", result["priority"])
        with col2:
            st.metric("Deadline", result["deadline"])
            st.metric("Time", result["time"])

        st.subheader("📝 Summary")
        st.write(result["summary"])

        st.subheader("🔑 Important Keywords")
        st.write(", ".join(result["keywords"]) if result["keywords"] else "No keywords found")

        st.subheader("📄 Original Notice")
        st.write(notice)
