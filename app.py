from flask import Flask, request, jsonify
from src.predict_model import predict

app = Flask(__name__)

@app.route("/")
def index():
    return "GEmstone Price Prediction API is running."

@app.route("/predict", methods=["POST"])
def predict_endpoint():
    try:
        input_json = request.get_json()
        required_keys = ['carat', 'cut', 'color', 'clarity', 'depth', 'table']
        if not all(k in input_json for k in required_keys):
            return jsonify({"error": "Missing one or more required fields."}), 400

        prediction = predict(input_json)
        return jsonify({"prediction":prediction}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=2000,debug=True)
