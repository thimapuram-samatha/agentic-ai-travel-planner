# 🌍 Agentic AI Travel Planner

An AI-powered travel planner that generates personalized itineraries based on your destination, budget, interests, travel style, and preferences.

## 🚀 Live Demo

👉 **[Try the AI Travel Planner](https://ai-powered-travel-planner-0902.streamlit.app)**

The application is deployed using Streamlit for the frontend and Render for the FastAPI backend.

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

## 🔗 Project Links

- 🌐 **Live Application:** [AI Travel Planner](https://ai-powered-travel-planner-0902.streamlit.app)
- ⚙️ **Backend API:** [FastAPI Backend](https://agentic-ai-travel-planner-x28s.onrender.com/)
- 💻 **GitHub Repository:** [Agentic AI Travel Planner](https://github.com/thimapuram-samatha/agentic-ai-travel-planner)

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

## 🌐 Deployment

The application is deployed using separate frontend and backend services.

## Frontend
- Streamlit Community Cloud
- Streamlit application
- `frontend/app.py`

## Backend
- Render
- FastAPI application
- `backend/main.py`

## 🔄 How It Works
##Architecture

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

- 🗺️ Add maps and location-based recommendations
- ☀️ Add weather information
- ✈️ Add real-time travel information
- 🏨 Add hotel and booking integrations
- 💳 Improve budget tracking
- 🤖 Add more AI travel agents

## 👩‍💻 Author

**Thimapuram Samatha**

Python Full Stack Developer with AI — Learning & Building AI-powered applications.
