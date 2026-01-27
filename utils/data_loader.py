import pandas as pd

def load_data():
    fake = pd.read_csv("data/Fake.csv")
    real = pd.read_csv("data/True.csv")

    fake['label'] = 1   # Fake
    real['label'] = 0   # Real

    df = pd.concat([fake, real], axis=0)
    df = df[['text', 'label']]

    return df
