from flask import Flask, request, jsonify
import pandas as pd
import joblib
from utils import train_model
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Putanje
DATA_PATH = "dataset/data.csv"
MODEL_PATH = "backend/model.pkl"

# Učitavanje ili treniranje modela
try:
    model = joblib.load(MODEL_PATH)
except:
    data = pd.read_csv(DATA_PATH)
    model = train_model(data, MODEL_PATH)
    
#Provjera da li Flask server ispravno radi
@app.route('/')
def home():
    return "Flask server is running!"

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json
    features = [[
        input_data['Godine'],
        input_data['GornjiKrvniiPritisak'],
        input_data['DonjiKrvniPritisak'],
        input_data['KoncentracijaGlukoze'],
        input_data['TempTijela'],
        input_data['OtkucajiSrca']
    ]]
    prediction = model.predict(features)[0]
    return jsonify({'prediction': prediction})

@app.route('/add-data', methods=['POST'])
def add_data():
    new_data = request.json
    global model

    # Pripremamo podatke za predikciju
    input_data = [
        new_data['Godine'],
        new_data['GornjiKrvniiPritisak'],
        new_data['DonjiKrvniPritisak'],
        new_data['KoncentracijaGlukoze'],
        new_data['TempTijela'],
        new_data['OtkucajiSrca']
    ]

    # Predikcija nivoa rizika
    predicted_risk = model.predict([input_data])[0]

    # Dodavanje nivoa rizika u nove podatke
    new_data['NivoRizika'] = predicted_risk

    # Učitavanje postojećeg dataset-a
    data = pd.read_csv(DATA_PATH)

    # Dodavanje novog reda u dataset
    new_row = pd.DataFrame([new_data])
    data = pd.concat([data, new_row], ignore_index=True)

    # Čuvanje ažuriranog dataset-a
    data.to_csv(DATA_PATH, index=False)

    # Retreniranje modela sa novim podacima
    model = train_model(data, MODEL_PATH)

    return jsonify({'message': 'Data added and model retrained successfully'})

if __name__ == "__main__":
    app.run(debug=True)
