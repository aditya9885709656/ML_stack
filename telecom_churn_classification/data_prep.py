#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
def pre_processing(data,target_column):
    #Converting categorical data to numeric data
    for column_name in data.columns:
        if(data[column_name].dtype == 'object'):
            data[column_name] = data[column_name].astype('category')
            data[column_name] = data[column_name].cat.codes
    #Removing duplicates
    data = data.drop_duplicates()
    #Removing null values
    data = data.dropna()
    #Intitilizing standard scaler object
    scaler = StandardScaler()
    #Normilizing all columns except target column
    features = data.columns[data.columns != target_column]
    data[features] = scaler.fit_transform(data[features])
    return data
    
    
