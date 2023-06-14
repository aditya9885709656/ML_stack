#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
def pre_processing(data):
    label_encoding = LabelEncoder()
    str_col = data.select_dtypes(include=('object')).columns
    for col in str_col:
        data[col] = label_encoding.fit_transform(data[col].astype('str'))
    return data
    
    
