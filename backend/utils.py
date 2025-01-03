import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(data, model_path):
    """
    Trenira Random Forest model i čuva ga na specificiranoj putanji.
    """
    X = data[['Godine', 'GornjiKrvniiPritisak', 'DonjiKrvniPritisak', 'KoncentracijaGlukoze', 'TempTijela', 'OtkucajiSrca']]
    y = data['NivoRizika']
    model = RandomForestClassifier()
    model.fit(X, y)
    joblib.dump(model, model_path)
    return model


