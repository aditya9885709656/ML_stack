#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
def pre_processing(data,target_column):
    #Getting important numeric columns based on correlation with saleprice
    important_numeric_cols = list(data.corr()[target_column][(data.corr()[target_column]>0.50) | (data.corr()[target_column]<-0.50)].index)
    #Getting important category columns
    category_cols = ["MSZoning", "Utilities","BldgType","Heating","KitchenQual","SaleCondition","LandSlope"]
    important_cols = important_numeric_cols + category_cols
    data = data[important_cols]
    data = pd.get_dummies(data, columns=category_cols)
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
    
    
