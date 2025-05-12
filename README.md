
# AI-Powered Wellness Recommendation System

This project is a Smart Recommendation System that provides personalized wellness suggestions based on user context like age, location, weather, mood, and more.

## 🧠 Features
- Predicts activities such as meditation, walking, hydration, etc.
- Uses a Random Forest model trained on synthetic data.
- Flask API for real-time recommendations.

## 📦 Folder Structure
```
wellness_recommender_project/
├── app/
│   └── wellness_recommender_api.py
├── model/
│   ├── wellness_recommender.pkl
│   └── encoder_*.pkl
├── requirements.txt
└── README.md
```

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the Flask server:
   ```bash
   python app/wellness_recommender_api.py
   ```

3. Use CURL to test:
   ```bash
   curl -X POST http://127.0.0.1:5000/recommend    -H "Content-Type: application/json"    -d '{
     "Age": 28,
     "Location": "Urban",
     "Weather": "Sunny",
     "TimeOfDay": "Morning",
     "Mood": "Stressed",
     "Occupation": "Student"
   }'
   ```

## ✅ Output
Returns a JSON with a personalized recommendation.
