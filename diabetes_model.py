import numpy as np
import joblib

class DiabetesPredictor:

    def __init__(self):
        self.model = joblib.load("real_model.pkl")
        self.scaler = joblib.load("scaler.pkl")

    def predict(self, input_data):

        features = np.array([[
            input_data['glucose'],
            input_data['bmi'],
            input_data['age'],
            input_data['systolic_bp'],
            input_data['family_history']
        ]])

        scaled = self.scaler.transform(features)

        pred = self.model.predict(scaled)[0]
        prob = self.model.predict_proba(scaled)[0][1]

        if pred == 0:
            label = "No Diabetes"
        else:
            label = "Diabetes Risk"

        stage, severity = self.get_stage(input_data)

        return {
            "classification": label,
            "risk_percentage": prob * 100,
            "stage": stage,
            "severity": severity
        }

    def get_stage(self, data):

        if data['hba1c'] < 5.7:
            return "Normal", "None"

        elif data['hba1c'] < 6.4:
            return "Prediabetes", "Mild"

        elif data['hba1c'] < 8:
            return "Type 2 (Early)", "Moderate"

        else:
            return "Type 2 (Advanced)", "Severe"
