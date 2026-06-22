import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score


def main():
    df = pd.read_csv("diabetes.csv")
    X = df[['Glucose','BMI','Age','BloodPressure','DiabetesPedigreeFunction']]
    y = df['Outcome']

    # Replace zeros with median (same preprocessing as training)
    for col in X.columns:
        X[col] = X[col].replace(0, X[col].median())

    scaler = joblib.load("scaler.pkl")
    model = joblib.load("real_model.pkl")

    X_scaled = scaler.transform(X)

    _, X_test, _, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    y_pred = model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nConfusion matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("\nClassification report:")
    print(classification_report(y_test, y_pred))


if __name__ == '__main__':
    main()
