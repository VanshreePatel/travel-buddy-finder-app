import streamlit as st
from datetime import datetime

# Initialize data
if "travel_buddies" not in st.session_state:
    st.session_state.travel_buddies = []

st.set_page_config(page_title="Travel Buddy Finder", page_icon="🌍", layout="centered")

# Sidebar Info
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/201/201623.png", width=80)
    st.title("Travel Buddy Finder")
    st.markdown("🌐 Connect with people going to the same destination!")
    st.markdown("---")
    st.info("Built with ❤️ using Streamlit")

# Title
st.markdown("<h1 style='text-align: center;'>🧳 Travel Buddy Finder</h1>", unsafe_allow_html=True)

# --- Form ---
with st.form("buddy_form"):
    st.subheader("🔍 Find or Add Your Travel Buddy")
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Your Name")
        gender = st.radio("Gender", ["👨‍🦰 Male", "👩‍🦰 Female", "🏳️‍🌈 Other"], horizontal=True)

    with col2:
        destination = st.selectbox("Destination", [
            "🇯🇵 Japan", 
            "🇫🇷 France", 
            "🇮🇹 Italy", 
            "🇮🇳 India", 
            "🇺🇸 USA", 
            "🇬🇧 UK",
            "🇹🇭 Thailand",
            "🇨🇦 Canada",
            "🇧🇷 Brazil",
            "🇦🇺 Australia",
            "🇿🇦 South Africa",
            "🇳🇿 New Zealand",
            "🇨🇭 Switzerland",
            "🇲🇽 Mexico",
            "🇸🇬 Singapore",
            "🌍 Other"
        ])
        travel_date = st.date_input("Planned Travel Date")

    bio = st.text_area("Short Bio / Preferences", max_chars=150)
    submit = st.form_submit_button("✨ Add Me")

    if submit and name and destination:
        buddy = {
            "name": name,
            "gender": gender,
            "destination": destination,
            "date": travel_date.strftime("%d %b %Y"),
            "bio": bio,
            "added": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        st.session_state.travel_buddies.append(buddy)
        st.success(f"{name} added as a travel buddy!")

# --- Display Buddies ---
st.markdown("## 🌟 Available Buddies")
if st.session_state.travel_buddies:
    for buddy in reversed(st.session_state.travel_buddies):
        with st.expander(f"👤 {buddy['name']} to {buddy['destination']}"):
            col1, col2 = st.columns([1, 4])
            with col1:
                st.markdown(f"### {buddy['gender']}")
                st.caption(f"🗓 {buddy['date']}")
            with col2:
                st.markdown(f"**Bio:** {buddy['bio']}")
                st.caption(f"Added: {buddy['added']}")
else:
    st.info("No buddies yet. Be the first to add your plan!")

# --- Footer ---
st.markdown("---")
st.markdown("<center>🚀 Happy Travels! | © 2025</center>", unsafe_allow_html=True)
