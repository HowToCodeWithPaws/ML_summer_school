from sklearn.linear_model import LogisticRegression
import pickle
from pickle import dump, load
import pandas as pd


def load_model_and_predict(df):
    with open('model.pickle', 'rb') as f:
        model = pickle.load(f)

    prediction = model.predict(df)[0]

    prediction_proba = model.predict_proba(df)[0]

    encode_prediction_proba = {
        0: "Вам не понравится с вероятностью",
        1: "Вам понравится с вероятностью"
    }

    encode_prediction = {
        0: "Увы, скорее всего Вам не понравится",
        1: "Ура! Вам понравится полёт"
    }

    prediction_data = {}
    for key, value in encode_prediction_proba.items():
        prediction_data.update({value: prediction_proba[key]})

    prediction_df = pd.DataFrame(prediction_data, index=[0])
    prediction = encode_prediction[prediction]

    return prediction, prediction_df


if __name__ == "__main__":
    print("")