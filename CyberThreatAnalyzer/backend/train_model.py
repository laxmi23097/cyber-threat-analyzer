import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Demo dataset with 3 features
# 0 = Normal, 1 = Threat
data = {
    'duration': [2, 10, 1, 15, 1, 30],
    'protocol': [0, 1, 0, 1, 0, 1],  # 0=tcp, 1=udp
    'packets': [50, 1500, 300, 2000, 70, 4000],
    'label': [0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[['duration', 'protocol', 'packets']]
y = df['label']

# Train Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained successfully and saved as model.pkl")