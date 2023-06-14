#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from datetime import datetime
# Define formula to calculate haversine distance
def distance(longitude1, latitude1, longitude2, latitude2):
    travel_dist = []
        
    for pos in range(len(longitude1)):
        long1,lati1,long2,lati2 = map(radians,[longitude1[pos],latitude1[pos],longitude2[pos],latitude2[pos]])
        dist_long = long2 - long1
        dist_lati = lati2 - lati1
        a = sin(dist_lati/2)**2 + cos(lati1) * cos(lati2) * sin(dist_long/2)**2
        c = 2 * asin(sqrt(a))*6371
        travel_dist.append(c)
    return travel_dist

def pre_processing(data):
    #Dropping the columns 'Unnamed: 0' and 'key' as well as NA rows
    data = data.drop(['Unnamed: 0','key'],axis=1)
    data.dropna(axis=0,inplace=True)
    # Calculate Haversine distance for each row and add distance in km as a new column
    data['distance_travelled'] = distance(data['pickup_longitude'].to_numpy(),data['pickup_latitude'].to_numpy(),data['dropoff_longitude'].to_numpy(),data['dropoff_latitude'].to_numpy()
    data['pickup_datetime']  = pd.to_datetime(data['pickup_datetime'])
    data['date'] = pd.to_datetime(data['pickup_datetime']).dt.date
    data['month'] = pd.to_datetime(data['pickup_datetime']).dt.month
    data['year'] = pd.to_datetime(data['pickup_datetime']).dt.year
    data['day_of_the_week'] = pd.to_datetime(data['pickup_datetime']).dt.weekday
    data['day_name'] = pd.to_datetime(data['pickup_datetime']).dt.day_name()
    data['pickup_time'] = pd.to_datetime(data['pickup_datetime']).dt.time
    data['pickup_hour'] = pd.to_datetime(data['pickup_datetime']).dt.hour
    data.drop(data[data['passenger_count'] > 5].index, axis=0, inplace = True)
    data.drop(data[data['passenger_count'] == 0].index, axis=0, inplace = True)
    data.drop(data[data['fare_amount'] < 2.5].index, axis=0, inplace = True)
    data.drop(data[data['distance_travelled'] > 130].index, axis=0, inplace = True)
    data.drop(data[data['distance_travelled'] == 0].index, axis=0, inplace = True)
    data.dropna(axis=0,inplace=True)
    data = data.drop(['pickup_datetime','pickup_time', 'date', 'pickup_longitude', 'pickup_latitude',
                  'dropoff_longitude', 'dropoff_latitude', 'day_name'],axis=1)
    return data
    
    
