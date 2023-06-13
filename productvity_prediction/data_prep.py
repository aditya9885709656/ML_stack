#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
def pre_processing(data):
    data['team'] = data['team'].astype(str)
    #Since value is 0 is majority in WIP(work in progress) colum, replacing null values with 0
    data['wip'].fillna(0, inplace=True)
    data['date'] = pd.to_datetime(data['date'])
    #All the data is from same year and only 3 different months, so we only extract the day of month as a numeric feature.
    data['date'] = data['date'].dt.day
    data['department'].replace('sweing', 'sewing', inplace=True)
    data['department'].replace('finishing ', 'finishing', inplace=True)
    #Removing outliers from wip and incentive
    data = data[data['wip'] <= 5000]
    data = data[data['incentive'] <= 5000]
    return data
    
    
