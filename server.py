import streamlit as st
from datetime import datetime

# Initialize session state
if "users" not in st.session_state:
    st.session_state.users = {}  # {username: password}
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "current_user" not in st.session_state:
    st.session_state.current_user = None
if "travel_buddies" not in st.session_state:
    st.session_state.travel_buddies = []

st.set_page_config(page_title="Travel Buddy Finder", page_icon="🌍", layout="centered")

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/201/201623.png", width=80)
    st.title("Travel Buddy Finder")
    if st.session_state.logged_in:
        st.success(f"Logged in as {st.session_state.current_user}")
        if st.button("🔓 Logout"):
            st.session_state.logged_in = False
            st.session_state.current_user = None
    st.markdown("---")
    st.info("Built with ❤️ using Streamlit")

# Title
st.markdown("<h1 style='text-align: center;'>🧳 Travel Buddy Finder</h1>", unsafe_allow_html=True)

# --- Login/Register ---
if not st.session_state.logged_in:
    option = st.radio("Choose Action", ["🔐 Login", "📝 Register"], horizontal=True)

    if option == "🔐 Login":
        st.subheader("Login to Your Account")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username in st.session_state.users and st.session_state.users[username] == password:
                st.session_state.logged_in = True
                st.session_state.current_user = username
                st.success("Logged in successfully!")
                st.experimental_rerun()
            else:
                st.error("Invalid username or password")

    else:
        st.subheader("Create a New Account")
        new_user = st.text_input("Create Username")
        new_pass = st.text_input("Create Password", type="password")
        if st.button("Register"):
            if new_user in st.session_state.users:
                st.warning("Username already exists")
            elif not new_user or not new_pass:
                st.warning("Please fill both fields")
            else:
                st.session_state.users[new_user] = new_pass
                st.success("Account created! Please login.")
else:
    # --- Travel Buddy Form ---
    with st.form("buddy_form"):
        st.subheader("🔍 Add Your Travel Buddy Info")
        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Your Name")
            gender = st.radio("Gender", ["👨‍🦰 Male", "👩‍🦰 Female", "🏳️‍🌈 Other"], horizontal=True)

        with col2:
            destination = st.selectbox("Destination", [
                "🇯🇵 Japan", "🇫🇷 France", "🇮🇹 Italy", "🇮🇳 India", "🇺🇸 USA", "🇬🇧 UK",
                "🇹🇭 Thailand", "🇨🇦 Canada", "🇧🇷 Brazil", "🇦🇺 Australia",
                "🇿🇦 South Africa", "🇳🇿 New Zealand", "🇨🇭 Switzerland",
                "🇲🇽 Mexico", "🇸🇬 Singapore", "🌍 Other"
            ])
            travel_date = st.date_input("Planned Travel Date")

        bio = st.text_area("Short Bio / Preferences", max_chars=150)
        submit = st.form_submit_button("✨ Add Me")

        if submit and name and destination:
            buddy = {
                "user": st.session_state.current_user,
                "name": name,
                "gender": gender,
                "destination": destination,
                "date": travel_date.strftime("%d %b %Y"),
                "bio": bio,
                "added": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            st.session_state.travel_buddies.append(buddy)
            st.success(f"{name} added as a travel buddy!")

    # --- Show Buddies ---
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
                    st.caption(f"Added: {buddy['added']} | User: {buddy['user']}")
    else:
        st.info("No buddies yet. Be the first to add your plan!")

# --- Footer ---
st.markdown("---")
st.markdown("<center>🚀 Happy Travels! | © 2025</center>", unsafe_allow_html=True)
