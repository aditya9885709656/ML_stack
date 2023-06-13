#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
def pre_processing(data,target_column):
    #Dropping car name column
    data = data.drop("car name", axis="columns")
    data["horsepower"] = pd.to_numeric(data["horsepower"], errors = "coerce")
    data["origin"] = data["origin"].astype("object")
    #Removing duplicates
    data = data.drop_duplicates()
    #Removing null values
    data = data.dropna()
    #Converting categorical data to numeric data
    for column_name in data.columns:
        if(data[column_name].dtype == 'object'):
            data[column_name] = data[column_name].astype('category')
            data[column_name] = data[column_name].cat.codes
    #Intitilizing standard scaler object
    scaler = StandardScaler()
    #Normilizing all columns except target column
    features = data.columns[data.columns != target_column]
    data[features] = scaler.fit_transform(data[features])
    return data
    
    
