#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
def pre_processing(data):
    #Creating month and year columns
    data['Month'] = data.YYYYMM.astype(str).str[4:6].astype(int)
    data['Year'] = data.YYYYMM.astype(str).str[0:4].astype(int)
    data.drop(['YYYYMM'], axis = 1, inplace = True)
    return data
    
    
