#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
def pre_processing(data,target_column):
    #Replacing MINIMUM_PAYMENTS null values with its median
    data['MINIMUM_PAYMENTS'].fillna(data['MINIMUM_PAYMENTS'].median(), inplace=True)
    data = data.dropna()
    data = data.drop(columns='CUST_ID')
    cols = data.columns
    scaler = MinMaxScaler()
    data = scaler.fit_transform(data)
    data = pd.DataFrame(data, columns=cols)
    return data
    
    
