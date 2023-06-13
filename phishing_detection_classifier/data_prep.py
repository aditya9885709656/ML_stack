#Import necessary libraries
import pandas as pd
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
    return data
    
    
