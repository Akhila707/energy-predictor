from flask import Flask, request, jsonify
import joblib
import numpy as np
import xgboost as xgb

app = Flask(__name__)

# Load XGBoost model
model = joblib.load("xgboost_model.pkl")  # make sure the filename matches

@app.route("/")
def home():
    return "🚀 XGBoost API is running! Use /predict."

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)
        features = np.array(data["features"]).reshape(1, -1)
        dmatrix = xgb.DMatrix(features)
        prediction = model.predict(dmatrix)
        return jsonify({"prediction": prediction.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
