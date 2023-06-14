#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
def pre_processing(data,target_column):
    #Converting categorical data to numeric data
    le = LabelEncoder()
    data['Index'] = le.fit_transform(data['Index'])
    return data
    
    
