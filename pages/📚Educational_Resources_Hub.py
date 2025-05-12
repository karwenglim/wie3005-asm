import streamlit as st
from PIL import Image

# --- Page setup ---
st.set_page_config(page_title="Educational Resources", page_icon="📚")
st.title("📚 Educational Resources Hub")
st.markdown("Resources curated by healthcare professionals to help patients understand their conditions better.")

# --- Sample hardcoded resources ---
resources = [
    {
        "title": "Understanding Hypertension",
        "description": "A beginner-friendly guide to managing high blood pressure.",
        "type": "Article",
        "link": "https://www.heart.org/en/health-topics/high-blood-pressure",
        "posted_by": "Dr. Smith",
        "src": "assets/HighBloodPressure.png"
    },
    {
        "title": "Diabetes & Nutrition",
        "description": "Learn how to manage diabetes through diet and exercise.",
        "type": "Video",
        "link": "https://www.youtube.com/watch?v=wZAjVQWbMlE",
        "posted_by": "Dr. Maria Tan",
        "src": "assets/Diabetes.png"
    },
    {
        "title": "Asthma Action Plan",
        "description": "Download a printable asthma management plan.",
        "type": "PDF",
        "link": "https://www.cdc.gov/asthma/action-plan/documents/asthma-action-plan-508.pdf",
        "posted_by": "Nurse Alex",
        "src": "assets/Asthma.png"
    }
]

# --- Display resources ---
st.subheader("Resources for You")
st.markdown("---")

for res in resources:
    with st.container():
        st.markdown(f"### [{res['title']}]({res['link']})")
        
        try:
            st.image(res["src"], use_container_width=True)
        except Exception as e:
            st.warning(f"Image not found for {res['title']}.")

        st.markdown(f"*Type:* {res['type']}  |  *Posted by:* {res['posted_by']}")
        st.markdown(res["description"])
        st.markdown("---")


# --- Simulate adding a new resource (not persistent) ---
st.subheader("📝 Submit a New Resource")

with st.form("resource_form"):
    title = st.text_input("Resource Title")
    description = st.text_area("Short Description")
    resource_type = st.selectbox("Resource Type", ["Article", "Video", "PDF", "Website", "Other"])
    link = st.text_input("Link to Resource (YouTube, PDF, article, etc.)")
    posted_by = st.text_input("Your Name / Role")

    submitted = st.form_submit_button("Submit Resource")

if submitted:
    st.success(f"Thank you {posted_by}, your resource has been added.")
    # st.info(f"Preview:\n- **Title**: {title}\n- **Type**: {resource_type}\n- **Link**: {link}")
