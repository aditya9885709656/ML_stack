#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
def pre_processing(data):
    Le = LabelEncoder()
    #Converting categorical data to numeric data
    data = data.drop(['job_ad_id','job_fed_contractor','job_req_min_experience'],axis=1)
    #DIVIDING THE COLUMNS INTO CATEGORICAL AND NUMERICAL LISTS
    categorical = []
    numerical = []
    for col in data.columns:
    if data[col].dtype == 'object':
        categorical.append(col)
    else:
        numerical.append(col)
    for col in categorical:
    if len(data[col].unique()) <= 3:
        data[col] = Le.fit_transform(data[col])
    else:
        freq_encoding = data[col].value_counts(normalize=True).to_dict()
        data[col] = data[col].map(freq_encoding)        
    return data
    
    
