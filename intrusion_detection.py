import pickle
import numpy as np

model = pickle.load(open("model/model.pkl","rb"))

def predict_attack(features):

    data = np.array(features).reshape(1,-1)

    prediction = model.predict(data)

    return prediction[0]