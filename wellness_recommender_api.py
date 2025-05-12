
from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load model and encoders
model = joblib.load("model/wellness_recommender.pkl")
encoders = {
    col: joblib.load(f"model/encoder_{col}.pkl")
    for col in ['Location', 'Weather', 'TimeOfDay', 'Mood', 'Occupation']
}
activity_decoder = joblib.load("model/encoder_RecommendedActivity.pkl")

# Create Flask app
app = Flask(__name__)

@app.route("/recommend", methods=["POST"])
def recommend():
    try:
        data = request.json
        # Extract and encode features
        features = [
            data["Age"],
            encoders['Location'].transform([data["Location"]])[0],
            encoders['Weather'].transform([data["Weather"]])[0],
            encoders['TimeOfDay'].transform([data["TimeOfDay"]])[0],
            encoders['Mood'].transform([data["Mood"]])[0],
            encoders['Occupation'].transform([data["Occupation"]])[0],
        ]
        # Predict
        pred = model.predict([features])[0]
        recommendation = activity_decoder.inverse_transform([pred])[0]

        return jsonify({"recommendation": recommendation})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
