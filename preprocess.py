import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data():

    data = pd.read_csv("dataset/iot_attack_dataset.csv")

    le = LabelEncoder()

    data["protocol"] = le.fit_transform(data["protocol"])
    data["service"] = le.fit_transform(data["service"])
    data["attack_type"] = le.fit_transform(data["attack_type"])

    return data