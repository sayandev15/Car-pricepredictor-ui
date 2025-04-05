from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("car_price_model.pkl")

features = [
    "Present_Price",
    "Kms_Driven",
    "Car_Age",
    "Fuel_Type_Diesel",
    "Fuel_Type_Petrol",
    "Seller_Type_Individual",
    "Transmission_Manual",
    "Owner"
]

@app.route('/')
def home():
    return "🚗 Car Price Prediction API is up and running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        input_data = [data.get(feature, 0) for feature in features]
        prediction = model.predict([input_data])
        predicted_price = round(prediction[0], 2)
        return jsonify({'predicted_price': predicted_price})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
