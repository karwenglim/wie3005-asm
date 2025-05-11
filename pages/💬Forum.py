import streamlit as st
from datetime import datetime
import uuid

st.set_page_config(layout="wide")
st.title("💬 Forum")

# Initialize session_state with hardcoded posts only once
if "posts" not in st.session_state:
    st.session_state.posts = [
        {
            "id": str(uuid.uuid4()),
            "user": "Alice",
            "avatar": "https://randomuser.me/api/portraits/women/1.jpg",
            "time": "2 hours ago",
            "content": "Has anyone experienced joint pain along with fever? I'm really worried it might be something serious.",
            "likes": 12,
            "comments": [
                {"user": "Bob", "avatar": "https://randomuser.me/api/portraits/men/2.jpg", "text": "That sounds like it could be an autoimmune issue. Have you seen a doctor?"},
                {"user": "Charlie", "avatar": "https://randomuser.me/api/portraits/men/3.jpg", "text": "Could be the flu, but I'd get it checked out just in case."}
            ]
        },
        {
            "id": str(uuid.uuid4()),
            "user": "Bob",
            "avatar": "https://randomuser.me/api/portraits/men/4.jpg",
            "time": "4 hours ago",
            "content": "I've been feeling fatigued for weeks now. My doctor ran tests, but they couldn’t pinpoint the cause. Any advice?",
            "likes": 8,
            "comments": [
                {"user": "Alice", "avatar": "https://randomuser.me/api/portraits/women/1.jpg", "text": "Fatigue can be linked to stress or even poor diet. Have you tried changing your routine?"},
                {"user": "Charlie", "avatar": "https://randomuser.me/api/portraits/men/5.jpg", "text": "You might want to consider seeing a specialist or getting a second opinion."}
            ]
        },
        {
            "id": str(uuid.uuid4()),
            "user": "Charlie",
            "avatar": "https://randomuser.me/api/portraits/men/5.jpg",
            "time": "1 day ago",
            "content": "Has anyone dealt with persistent headaches? I’ve tried over-the-counter meds, but nothing seems to work.",
            "likes": 5,
            "comments": [
                {"user": "Alice", "avatar": "https://randomuser.me/api/portraits/women/1.jpg", "text": "I had similar issues. I was prescribed a migraine medication, and it really helped."},
                {"user": "Bob", "avatar": "https://randomuser.me/api/portraits/men/4.jpg", "text": "Have you tried keeping a headache journal? It could help identify triggers."}
            ]
        },
        {
            "id": str(uuid.uuid4()),
            "user": "Alice",
            "avatar": "https://randomuser.me/api/portraits/women/1.jpg",
            "time": "3 days ago",
            "content": "I’ve been struggling with anxiety lately. I know exercise is good, but I feel too overwhelmed to start.",
            "likes": 15,
            "comments": [
                {"user": "Bob", "avatar": "https://randomuser.me/api/portraits/men/2.jpg", "text": "Starting small with a 10-minute walk could help ease the pressure. Baby steps!"},
                {"user": "Charlie", "avatar": "https://randomuser.me/api/portraits/men/5.jpg", "text": "Yoga and mindfulness also helped me when I felt anxious."}
            ]
        },
        {
            "id": str(uuid.uuid4()),
            "user": "Bob",
            "avatar": "https://randomuser.me/api/portraits/men/4.jpg",
            "time": "5 days ago",
            "content": "Does anyone know how to manage asthma symptoms during cold weather? I’m really struggling this winter.",
            "likes": 9,
            "comments": [
                {"user": "Alice", "avatar": "https://randomuser.me/api/portraits/women/1.jpg", "text": "Make sure to use your inhaler regularly and wear a scarf over your mouth to warm up the air."},
                {"user": "Charlie", "avatar": "https://randomuser.me/api/portraits/men/5.jpg", "text": "You should also avoid cold, dry air as much as possible and stay indoors when you can."}
            ]
        },
        {
            "id": str(uuid.uuid4()),
            "user": "Charlie",
            "avatar": "https://randomuser.me/api/portraits/men/5.jpg",
            "time": "1 week ago",
            "content": "Has anyone been on a gluten-free diet for a while? How did you adjust to it and feel? I’ve been considering it.",
            "likes": 7,
            "comments": [
                {"user": "Alice", "avatar": "https://randomuser.me/api/portraits/women/1.jpg", "text": "It took a while for me to get used to it, but my digestive issues improved."},
                {"user": "Bob", "avatar": "https://randomuser.me/api/portraits/men/4.jpg", "text": "Gluten-free can be tough, but it definitely helps with inflammation if you’re sensitive."}
            ]
        },
        {
            "id": str(uuid.uuid4()),
            "user": "Alice",
            "avatar": "https://randomuser.me/api/portraits/women/1.jpg",
            "time": "1 week ago",
            "content": "I’ve been having trouble sleeping lately. Any tips for getting better sleep without relying on medication?",
            "likes": 10,
            "comments": [
                {"user": "Bob", "avatar": "https://randomuser.me/api/portraits/men/2.jpg", "text": "Try limiting screen time before bed and establish a consistent routine. It helps a lot."},
                {"user": "Charlie", "avatar": "https://randomuser.me/api/portraits/men/5.jpg", "text": "I also found drinking chamomile tea before bed really soothing."}
            ]
        }
    ]


# --- Custom CSS ---
st.markdown("""
    <style>
        .post-box {
            background-color: #1e1e1e;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 25px;
            border: 1px solid #333;
        }
        .user-img, .comment-avatar {
            border-radius: 50%;
        }
        .comment-avatar {
            margin-right: 10px;
        }
        .text-small {
            color: #999;
            font-size: 13px;
        }
        .like-text {
            color: #e74c3c; /* Red color for heart */
            font-size: 14px;
        }
        .comment-box {
            display: flex;
            align-items: flex-start;
            margin-top: 10px;
        }
        .comment-content {
            font-size: 14px;
            color: #ccc;
        }
    </style>
""", unsafe_allow_html=True)

# --- Post New Status ---
st.subheader("📢 Share your thoughts")
new_status = st.text_area("What's on your mind?", key="status_input")
if st.button("Post"):
    if new_status.strip():
        st.session_state.posts.insert(0, {
            "id": str(uuid.uuid4()),
            "user": "You",
            "avatar": "https://randomuser.me/api/portraits/lego/1.jpg",
            "time": datetime.now().strftime("%H:%M %p"),
            "content": new_status,
            "likes": 0,
            "comments": []
        })
        st.success("Posted successfully!")
        st.rerun()
    else:
        st.warning("Please write something before posting.")

st.markdown("---")

# --- Display Posts ---
for post in st.session_state.posts:
    comments_html = ""
    for comment in post["comments"]:
        comments_html += f"""
        <div class="comment-box">
            <img src="{comment['avatar']}" width="35" class="comment-avatar"/>
            <div class="comment-content"><strong>{comment['user']}</strong><br>{comment['text']}</div>
        </div>
        """.strip()

    post_html = f"""
    <div class="post-box">
        <div style="display:flex;align-items:center;gap:15px;">
            <img src="{post['avatar']}" width="50" class="user-img"/>
            <div>
                <strong>{post['user']}</strong><br>
                <span class="text-small">{post['time']}</span>
            </div>
        </div>
        <p style="margin-top:10px;font-size:15px;">{post['content']}</p>
        <span class="like-text">❤️ {post['likes']} Hearts</span>
        {comments_html}
    </div>
    """
    st.markdown(post_html, unsafe_allow_html=True)

    # --- Add Heart Button ---
    like_button_key = f"like_btn_{post['id']}"
    if st.button("❤️ Like", key=like_button_key):
        post["likes"] += 1
        st.rerun()

    # --- Add Comment Input for This Post ---
    comment_input_key = f"comment_input_{post['id']}"
    comment_button_key = f"comment_btn_{post['id']}"
    comment_input = st.text_input("Write a comment...", key=comment_input_key)
    if st.button("Comment", key=comment_button_key):
        if comment_input.strip():
            post["comments"].append({
                "user": "You",
                "avatar": "https://randomuser.me/api/portraits/lego/2.jpg",
                "text": comment_input
            })
            st.rerun()
        else:
            st.warning("Comment cannot be empty.")

    st.markdown("---")

