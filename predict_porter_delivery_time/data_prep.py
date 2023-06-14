#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
def pre_processing(df):
    df.drop('store_id',axis=1,inplace=True)
    df.dropna(inplace=True)
    df.created_at = pd.to_datetime(df.created_at)
    df.actual_delivery_time = pd.to_datetime(df.actual_delivery_time)
    df['Available_delivery_Time_seconds'] = (df.actual_delivery_time - df.created_at).dt.total_seconds().astype('int64')
    df.store_primary_category = df.store_primary_category.astype('object')
    df.market_id = df.market_id.astype('object')
    df.order_protocol = df.order_protocol.astype('object')
    return df
    
    
