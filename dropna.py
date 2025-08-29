import pandas as pd

def clean_data(file):
    data = pd.read_csv(file)
    data.dropna(inplace=True)
    data.to_csv("cleaned.csv")
