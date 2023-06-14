#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
def pre_processing(data):
    le = LabelEncoder()
    data['Region'] = le.fit_transform(data['Region'])
    data['Region'].unique()
    data['Income group'] = le.fit_transform(data['Income group'])
    data['Political regime'] = le.fit_transform(data['Political regime'])
    return data
    
    
