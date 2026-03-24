from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pickle
import os

app = Flask(__name__)
CORS(app)

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Favicon route
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.abspath(os.path.dirname(__file__)), 'favicon.ico')

# Prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    try:
        duration = float(data.get("duration", 0))
        protocol = int(data.get("protocol", 0))
        packets = float(data.get("packets", 0))

        prediction = model.predict([[duration, protocol, packets]])
        result = "Threat Detected" if prediction[0] == 1 else "Normal Traffic"

        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)