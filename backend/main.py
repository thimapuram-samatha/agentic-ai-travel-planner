# python -m pip install uvicorn
# python -m pip install fastapi
# python -m pip install langchain_groq

from fastapi import FastAPI 
from langchain_groq import ChatGroq
import os

app = FastAPI() # creating fastapi object

llm = ChatGroq(
    model = "openai/gpt-oss-120b",
    api_key = os.getenv("GROQ_API_KEY")
)
@app.get("/")
def home():
    return {"message" : "AI-Powered Travel Planner Backend is running!"}

@app.post("/plan_trip")
def plan_trip(payload : dict):
    
    prompt = f"""
You are an intelligent AI Travel Planner.

Create a personalized, practical, and easy-to-follow travel itinerary using the user's information below.

TRIP DETAILS
-------------
Starting Location: {payload["starting_location"]}
Destination: {payload["destination_location"]}
Trip Duration: {payload["no_of_trip_days"]} days
Number of Travelers: {payload["no_of_people"]}
Travel Style: {payload["travel_style"]}
Budget: ₹{payload["budget"]}
Interests: {payload["interests"]}
Accommodation Preference: {payload["accommodation"]}
Food Preferences: {payload["food_preferences"]}
Preferred Transportation: {payload["transport"]}
Extra Information: {payload["extra_information"]}

Create a realistic itinerary that matches the user's interests, travel style, number of days, and budget.

FORMAT THE RESPONSE EXACTLY LIKE THIS:

🌍 Trip Overview

Give a short summary of the trip.

📅 Day 1
🌅 Morning
- Places to visit
- Activities

☀️ Afternoon
- Places to visit
- Activities

🌙 Evening
- Places to visit
- Activities
🍴 Food
- Recommended food or restaurants

💰 Estimated Cost
- Give an approximate cost for the day.

Repeat the same format for every day of the trip.

🏨 Accommodation
- Recommended area to stay
- Suitable accommodation type
- Approximate cost per night
- Reason for the recommendation

🍴 Food Recommendations
- Breakfast suggestions
- Lunch suggestions
- Dinner suggestions
- Local specialties to try

🚗 Transportation
- Best way to travel from the starting location to the destination
- Best local transportation options
- Approximate transportation cost

💰 Estimated Budget
Break down the estimated total cost into:
- 🚗 Transportation
- 🏨 Accommodation
- 🍴 Food
- 🎟️ Activities
- 💰 Total Estimated Cost

💡 Travel Tips
Provide 5 useful tips for this trip.
Consider the extra information provided by the user when creating the itinerary.

IMPORTANT INSTRUCTIONS
----------------------
- Keep the itinerary realistic and practical.
- Prioritize places based on the user's interests.
- Respect the user's travel style and budget.
- Avoid unnecessary information.
- Use clear headings and bullet points.
- Keep paragraphs short and easy to read.
- Give approximate costs in Indian Rupees (₹).
- Do not use tables.
- Do not write one large paragraph.
- Make the final response neat, organized, and easy to understand.
- Return the response using Markdown only.
- Do not use HTML tags.

- Return only plain text.
- Do not use <h1>, <h2>, <h3>, <p>, <div>, or any other HTML tags in response.

"""
    
    response = llm.invoke(prompt)
    return {"travel_plan": response.content} 