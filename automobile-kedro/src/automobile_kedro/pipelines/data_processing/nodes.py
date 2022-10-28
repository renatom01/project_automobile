"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.3
"""
import pandas as pd
from typing import Dict
from sklearn.preprocessing import OrdinalEncoder

def preprocess_encoding(df: pd.DataFrame):
    "This function converts categorical features into numeric features"
    ordinal_encoder = OrdinalEncoder()
    features = [
            'normalized-losses',  'make', 'fuel-type', 'aspiration', 
            'num-of-doors', 'body-style', 'drive-wheels', 'engine-location',
            'engine-type' , 'num-of-cylinders', 'fuel-system', 'bore', 'stroke',
             'horsepower', 'peak-rpm', 'price'     
           ] 
    df[features]= ordinal_encoder.fit_transform(df[features])
    return df, ordinal_encoder