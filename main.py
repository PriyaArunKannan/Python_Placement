import streamlit as st
from src.data_manager import DBManager

st.set_page_config(page_title="Placement Dashboard", layout="wide")
st.title("🎓 Placement Eligibility & Insights Dashboard")

# Initialize DB
db = DBManager()

# --- SIDEBAR: Filters & Insights ---
st.sidebar.header("🔧 Filters & Insights")

view_mode = st.sidebar.radio("Select View Mode", ["Eligibility Filter", "SQL Insight"])

# --- Get data depending on the selected view ---
if view_mode == "Eligibility Filter":
    st.sidebar.subheader("🎯 Eligibility Criteria")
    min_problems = st.sidebar.slider("Minimum Problems Solved", 0, 100, 50)
    min_soft_skills = st.sidebar.slider("Minimum Avg Soft Skill Score", 0, 100, 75)
    min_mock_score = st.sidebar.slider("Minimum Mock Interview Score", 0, 100, 60)
    min_internships = st.sidebar.slider("Minimum Assessment Completed", 0, 10, 1)
    placement_status = st.sidebar.selectbox("Placement Status", ["Any", "Ready", "Placed", "Not Ready"])
    batch_filter = st.sidebar.selectbox("Select Batch", ["All"] + db.get_all_batches())
    grad_year = st.sidebar.selectbox("Graduation Year", ["All"] + db.get_all_graduation_years())

    # Fetch eligible students
    df = db.get_eligible_students2(
        min_problems=min_problems,
        min_soft_skills=min_soft_skills,
        min_mock_score=min_mock_score,
        min_internships=min_internships,
        placement_status=placement_status,
        batch_filter=batch_filter,
        grad_year=grad_year
    )

    st.subheader("📋 Eligible Students")
    if df.empty:
        st.warning("No students match the selected criteria.")
    else:
        st.dataframe(df)

else:
    st.sidebar.subheader("📊 Select Insight")
    queries = db.get_insights()
    selected_insight = st.sidebar.selectbox("Insight", list(queries.keys()))

    # Fetch insight result
    result_df = db.run_query(queries[selected_insight])

    st.subheader(f"📈 Insight: {selected_insight}")
    if result_df.empty:
        st.info("No data found for this insight.")
    else:
        st.dataframe(result_df)

