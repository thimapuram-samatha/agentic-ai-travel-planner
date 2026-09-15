# 🌍 Agentic AI Travel Planner

An AI-powered travel planner that generates personalized itineraries based on your destination, budget, interests, travel style, and preferences.

## ✨ Features

- 🌍 Personalized travel itineraries
- 📅 Day-by-day trip planning
- 💰 Budget estimation
- 🏨 Accommodation recommendations
- 🍴 Food recommendations
- 🚗 Transportation suggestions
- 🎯 Interest-based travel planning
- 💡 Useful travel tips
- 🤖 AI-generated travel plans

## 🛠️ Technologies Used

- Python
- Streamlit
- FastAPI
- LangChain
- Groq
- Requests
- Markdown

## 🏗️ Project Structure

```text
AGENTIC_AI_TRAVEL_PLANNER
│
├── backend
│   ├── main.py
│   └── requirements.txt
│
├── frontend
│   ├── app.py
│   └── requirements.txt
│
├── .gitignore
└── README.md

## 🔄 How It Works

```text
User
  ↓
Streamlit Frontend
  ↓
FastAPI Backend
  ↓
LangChain + Groq
  ↓
AI Generated Travel Plan
  ↓
Streamlit Frontend
  ↓
User

## 📋 Trip Planning Inputs

The application allows users to provide:

- 📍 Starting Location
- 📍 Destination
- 📅 Trip Duration
- 👥 Number of Travelers
- 🧳 Travel Style
- 💰 Travel Budget
- 🎯 Travel Interests
- 🏡 Accommodation Preference
- 🍛 Food Preference
- 🚗 Preferred Transportation
- 📝 Extra Information / Special Requirements

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/thimapuram-samatha/agentic-ai-travel-planner.git
cd agentic-ai-travel-planner

# Install Backend Dependencies

cd backend
pip install -r requirements.txt

# Configure the Groq API Key

$env:GROQ_API_KEY="YOUR_GROQ_API_KEY"

# Start the FastAPI Backend
python -m uvicorn main:app --reload

# Install Frontend Dependencies

cd frontend
pip install -r requirements.txt

# Start the Streamlit Frontend

streamlit run app.py

## 🔐 Environment Variables & Security

This project uses the Groq API to generate AI-powered travel plans.

The application requires the following environment variable:

```text
GROQ_API_KEY

## 📌 Future Improvements

- 🌐 Deploy the application online
- 🗺️ Add maps and location-based recommendations
- ☀️ Add weather information
- ✈️ Add real-time travel information
- 🏨 Add hotel and booking integrations
- 💳 Improve budget tracking
- 🤖 Add more AI travel agents

## 👩‍💻 Author

**Thimapuram Samatha**

Python Full Stack Developer with AI — Learning & Building AI-powered applications.