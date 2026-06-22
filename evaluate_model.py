import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# Load data
df = pd.read_csv("diabetes.csv")
X = df[['Glucose','BMI','Age','BloodPressure','DiabetesPedigreeFunction']]
y = df['Outcome']

# Replace zeros with median (same preprocessing as training)
for col in X.columns:
    X[col] = X[col].replace(0, X[col].median())

# Load scaler and model
scaler = joblib.load('scaler.pkl')
model = joblib.load('real_model.pkl')

# Scale features
X_scaled = scaler.transform(X)

# Train/test split (same split as training)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Predict
y_pred = model.predict(X_test)

# Metrics
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {acc:.4f}")
print("\nConfusion Matrix:")
print(cm)
print("\nClassification Report:")
print(report)
