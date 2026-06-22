import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from datetime import datetime


def main():
    df = pd.read_csv("diabetes.csv")
    X = df[['Glucose','BMI','Age','BloodPressure','DiabetesPedigreeFunction']]
    y = df['Outcome']

    for col in X.columns:
        X[col] = X[col].replace(0, X[col].median())

    scaler = joblib.load("scaler.pkl")
    model = joblib.load("real_model.pkl")

    X_scaled = scaler.transform(X)
    _, X_test, _, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    out_lines = []
    out_lines.append(f"Metrics generated: {datetime.now().isoformat()}")
    out_lines.append(f"Accuracy: {acc:.6f}")
    out_lines.append("\nConfusion matrix:")
    out_lines.append(str(cm))
    out_lines.append("\nClassification report:")
    out_lines.append(report)

    with open('metrics.txt', 'w') as f:
        f.write('\n'.join(out_lines))

    print("Saved metrics to metrics.txt")


if __name__ == '__main__':
    main()
