from flask import Flask, request, jsonify
from flask_cors import CORS
from src.predict_model import predict
import numpy as np

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "*"}})

@app.route("/")
def index():
    return "GEmstone Price Prediction API is running."

@app.route("/predict", methods=["POST"])
def predict_endpoint():
    try:

        data = request.get_json(force=True)

        required_keys = ['carat', 'cut', 'color', 'clarity', 'depth', 'table']
        missing = [k for k in required_keys if k not in data]
        if missing:
            return jsonify({"error": f"missing required field: {missing}"}), 400
        
        try:
            carat = float(data['carat'])
            depth = float(data['depth'])
            table = float(data['table'])
        except (ValueError, TypeError):
            return jsonify({"error": 'Carat, Depth, and Table must be valid numbers.'}), 400
        
        if np.isnan(carat) or np.isnan(depth) or np.isnan(table):
            return jsonify({"error": 'numeric fields contain NaN.'}), 400
        
        
        try:
            prediction = predict(data)
            print(prediction)
        except ValueError as ve:
            return jsonify({"error": str(ve)}), 400

    
        return jsonify({"prediction":prediction}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=2000,debug=True)
