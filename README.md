# Car Price Predictor

A machine learning application that predicts the selling price of used cars based on various features.

## Features

- Predicts car prices based on:
  - Present price (in Lakhs)
  - Kilometers driven
  - Car age (in years)
  - Fuel type (Petrol/Diesel/CNG)
  - Seller type (Dealer/Individual)
  - Transmission type (Manual/Automatic)
  - Number of previous owners

## Technologies Used

- Python
- Flask (Backend API)
- Streamlit (User Interface)
- Scikit-learn (Machine Learning)
- Joblib (Model Serialization)

## How to Run Locally

1. Clone the repository:
   ```
   git clone https://github.com/sayandev15/Car-pricepredictor-ui.git
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Flask API:
   ```
   python app.py
   ```

4. In a separate terminal, run the Streamlit UI:
   ```
   streamlit run streamlit_app.py
   ```

5. Access the application at http://localhost:8501 in your browser. 