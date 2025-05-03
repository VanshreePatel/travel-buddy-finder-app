import streamlit as st
import pandas as pd
from datetime import datetime
import os

# File to store data
CSV_FILE = "buddies.csv"

# Load existing data
if os.path.exists(CSV_FILE):
    df = pd.read_csv(CSV_FILE)
else:
    df = pd.DataFrame(columns=["Name", "Gender", "Destination", "Date", "Bio", "Added"])

st.set_page_config(page_title="Travel Buddy Finder", page_icon="🌍")

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/201/201623.png", width=80)
st.sidebar.title("Travel Buddy Finder")
st.sidebar.markdown("🌐 Connect with people going to the same destination!")

st.markdown("<h1 style='text-align: center;'>🧳 Travel Buddy Finder</h1>", unsafe_allow_html=True)

with st.form("form"):
    st.subheader("🔍 Add Your Travel Buddy Info")
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Your Name")
        gender = st.radio("Gender", ["👨‍🦰 Male", "👩‍🦰 Female", "🏳️‍🌈 Other"], horizontal=True)
    with col2:
        destination = st.selectbox("Destination", [
            "🇯🇵 Japan", "🇫🇷 France", "🇮🇹 Italy", "🇮🇳 India", "🇺🇸 USA", "🇬🇧 UK",
            "🇹🇭 Thailand", "🇨🇦 Canada", "🇧🇷 Brazil", "🇦🇺 Australia",
            "🇿🇦 South Africa", "🇳🇿 New Zealand", "🇨🇭 Switzerland", "🇲🇽 Mexico",
            "🇸🇬 Singapore", "🌍 Other"
        ])
        date = st.date_input("Planned Travel Date")

    bio = st.text_area("Short Bio", max_chars=150)
    submit = st.form_submit_button("✨ Add Me")

    if submit and name:
        new_row = {
            "Name": name,
            "Gender": gender,
            "Destination": destination,
            "Date": date.strftime("%d %b %Y"),
            "Bio": bio,
            "Added": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(CSV_FILE, index=False)
        st.success("🎉 Travel buddy added!")

# Show buddies
st.markdown("## 🌟 Available Travel Buddies")
if not df.empty:
    for _, buddy in df[::-1].iterrows():
        with st.expander(f"👤 {buddy['Name']} to {buddy['Destination']}"):
            st.markdown(f"**Gender:** {buddy['Gender']}")
            st.markdown(f"**Date:** {buddy['Date']}")
            st.markdown(f"**Bio:** {buddy['Bio']}")
            st.caption(f"Added: {buddy['Added']}")
else:
    st.info("No buddies yet. Be the first!")

st.markdown("---")
st.markdown("<center>🚀 Happy Travels! | © 2025</center>", unsafe_allow_html=True)
