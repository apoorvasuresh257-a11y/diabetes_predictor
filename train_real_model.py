import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib

print("Loading dataset...")

df = pd.read_csv("diabetes.csv")

# Use only user-friendly features
X = df[['Glucose','BMI','Age','BloodPressure','DiabetesPedigreeFunction']]
y = df['Outcome']

# Fix zero values
for col in X.columns:
    X[col] = X[col].replace(0, X[col].median())

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

# Save
joblib.dump(model, "real_model.pkl")
joblib.dump(scaler, "scaler.pkl")

acc = model.score(X_test, y_test)
print(f"✅ Training completed | Accuracy: {acc:.2f}")
print("Model saved successfully!")
