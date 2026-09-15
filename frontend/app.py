import streamlit as st

import requests as req

import markdown

import re

st.markdown("""
<style>
.stApp{
background-image:
url("https://wallpapercave.com/wp/wp12448539.jpg");
background-size : cover;
background-position : center;
background-attachment : fixed;}
/* Main title */
h1 {
    color: white !important;
    text-shadow: 2px 2px 5px black;
}

/* Subheading */
h2, h3 {
    color: white !important;
    text-shadow: 2px 2px 4px black;
}

/* Normal text */
.stApp p {
color : white !important;
}

.stButton > button {
    background-color : black;
    color: white !important;
    border-radius: 10px;
    border: none;
    padding: 10px 25px;
    font-size: 18px;
    font-weight: bold;

}
</style>
""", unsafe_allow_html = True)

st.title("🌍 AI-POWERED TRAVEL PLANNER")

st.subheader("Plan Smarter, Travel Better - Create Personalized Itineraries With Generative AI. ✈️")

starting_location = st.text_input("📍 Enter Your Starting Location", placeholder = "Enter Your Starting City")
destination_location = st.text_input("📍 Enter Your Destination Location", placeholder = "Enter Your Destination City")
no_of_trip_days = st.number_input("📅Trip Duration", min_value = 1, step = 1)
no_of_people = st.number_input("👥Number of Travelers", min_value = 1, step = 1)
budget = st.number_input("💸Enter Your Travel Budget", min_value = 0, step = 1000)
travel_style = st.selectbox("🧳 Travel Style", ["Select", "Any", "Budget", "Standard", "Luxury", "Relaxed"])
interests = st.multiselect("🎯 Travel Interests", ["beaches", "Historical Places", "Parties", "Nature", "Adventure", "Food","Shopping", "Culture","Nightlife", "Trekking"])
accommodation = st.selectbox("🏡 Accommodation Preference", ["Select", "Any","Hotel", "Resort", "Hostel"])
food_preferences = st.selectbox("🍛 Food Preference", ["Select", "Any", "Vegetarian", "Non-Vegetarian", "Vegan"])
transport = st.selectbox("🚗 Preferred Transportation", ["Select", "Any","Car", "Bus", "Train", "Flight", "Bike"])
extra_information = st.text_area(
    "📝 Extra Information",placeholder="Enter any additional requirements or preferences for your trip...")

button = st.button("✨ Generate My Travel Plan")
if button:
    st.write("Generating Your Personalized Travel Plan..")
    payload = {
        "starting_location" : starting_location,
        "destination_location" : destination_location,
        "no_of_trip_days" : no_of_trip_days,
        "no_of_people" : no_of_people,
        "travel_style" :travel_style,
        "budget" : budget,
        "interests" : interests,
        "accommodation" : accommodation,
        "food_preferences" : food_preferences,
        "transport" : transport,
        "extra_information": extra_information
    }
    response = req.post("https://agentic-ai-travel-planner-x28s.onrender.com/plan_trip", json = payload)
    if response.status_code != 200:
        st.error(f"Backend Error: {response.status_code}")
        st.code(response.text)
        st.stop()

    st.success("✅ Travel Plan Generated Successfully!")

    travel_plan = response.json()["travel_plan"]

    travel_plan = travel_plan.replace("**", "")
    travel_plan = re.sub(r"```(?:html|markdown)?\s*", "", travel_plan)
    travel_plan = re.sub(r"\s*```", "", travel_plan)

    travel_plan = re.sub(r"<[^>]+>", "", travel_plan)
    
    st.markdown(
        """
        <style>
        .travel-box {
            background-color: white;
            padding: 30px;
            border-radius: 15px;
            margin-top: 20px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
            color: black;
        }
        .travel-box h1,
        .travel-box h2,
        .travel-box h3,
        .travel-box p,
        .travel-box li {
            color: black !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    travel_html = markdown.markdown(
        travel_plan,
        extensions = ["extra"]
    )

    st.markdown(
        f"""
        <div class="travel-box">
        
        ✈️ Your Personalized Travel Plan
        {travel_plan}
        </div>
        """,
        unsafe_allow_html=True
    )
