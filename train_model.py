import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix

import seaborn as sns
import matplotlib.pyplot as plt


# Load dataset
data = pd.read_csv("dataset/iot_attack_dataset.csv")

# Encode categorical features
le = LabelEncoder()

data["protocol"] = le.fit_transform(data["protocol"])
data["service"] = le.fit_transform(data["service"])
data["attack_type"] = le.fit_transform(data["attack_type"])

# Features and label
X = data.drop("attack_type", axis=1)
y = data["attack_type"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=20,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# Predictions
pred = model.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(y_test, pred)

sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()

# Save model
pickle.dump(model, open("model/model.pkl", "wb"))