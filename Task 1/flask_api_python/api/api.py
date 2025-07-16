
from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
def load_model(path="iris_model.pkl"):
    with open(path, 'rb') as file:
        return pickle.load(file)

model = load_model()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        feature_array = data.get('feature_array')

        if not feature_array or not isinstance(feature_array, list):
            return jsonify({"error": "Invalid or missing 'feature_array'"}), 400

        prediction = model.predict([feature_array]).tolist()
        return jsonify({"prediction": prediction})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "API is working"}), 200

@app.route('/info', methods=['GET'])
def info():
    return jsonify({
        "model_type": "RandomForestClassifier",
        "input_format": "[sepal_length, sepal_width, petal_length, petal_width]",
        "output": "Iris class (0, 1,,2)"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
