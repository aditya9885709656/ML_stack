#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
def pre_processing(data):
    #Dropping ID column
    data.drop('Unnamed: 0',axis=1,inplace=True)
    # Convert the categorical values in the dataframe to numerical codes. 

    for col in data[['Employment Type', 'GraduateOrNot','FrequentFlyer','EverTravelledAbroad']].columns:
      new_df = pd.get_dummies(data[col])
      data = pd.concat([data, new_df], axis=1)
      data = data.drop([col], axis=1)
    
    return data
    
    
