#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
def pre_processing(data):
    le = LabelEncoder()
    data['Gender'] = le.fit_transform(data['Gender'])
    data['VRHeadset'] = le.fit_transform(data['VRHeadset'])
    data['ImmersionLevel'] = le.fit_transform(data['ImmersionLevel'])
    return data
    
    
