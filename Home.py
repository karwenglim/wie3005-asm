import streamlit as st

# Set the page config for a better layout and title
st.set_page_config(page_title="Healthcare Multi-Page App", layout="wide")

# Title and header for the landing page
st.title("Welcome to the Healthcare Multi-Page App")
st.header("Explore, Engage, and Learn")

# Add a welcome message to introduce users to the app
st.markdown("""
    This is a simple healthcare platform built with Streamlit. 
    You can explore discussions in the **Forum**, 
    or interact with the **AI Assistant** for medical-related inquiries.
    Select a page from the sidebar to get started!
""")

# Add a logo or an image (optional)

# Instructions or some CTA (Call to Action) message
st.markdown("""
    Explore different pages of the app to interact with:
    - **Forum**: Share and discuss medical topics, symptoms, and healthcare issues with others.
    - **AI Assistant**: Ask health-related questions and get automated responses.
    
    Choose a page from the sidebar to begin your journey.
""")

# Sidebar enhancements
st.sidebar.title("Navigation")
st.sidebar.write("Please choose a page from the options below:")

# Add descriptive buttons or links
st.sidebar.markdown("### Pages")
st.sidebar.markdown("[Forum](pages/Forum.py)", unsafe_allow_html=True)
st.sidebar.markdown("[AI Assistant](pages/AI_Assistant.py)", unsafe_allow_html=True)

# You can also add some custom styling if you want
st.markdown("""
    <style>
        .main {
            padding-top: 2rem;
            font-size: 18px;
        }
        h1 {
            font-weight: 600;
        }
        h2 {
        }
        .stImage {
            border-radius: 8px;
        }
        .stMarkdown {
            font-size: 16px;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Optional: Add a footer or contact information at the bottom
st.markdown("""
    ---
    **Contact Us**: support@healthcareapp.com
""")
