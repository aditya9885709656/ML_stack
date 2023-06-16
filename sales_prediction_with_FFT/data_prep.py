#Import necessary libraries
import pandas as pd
from darts import TimeSeries
from darts.models import FFT
from darts.metrics import mae
def pre_processing(data):
    data = data.groupby('Date').sum()
    data['Date'] = data.index
    data = data[['Date','TotalSales']]

    data['Date'] = pd.to_datetime(data['Date'],format = '%Y-%m-%d')
    #convert the pandas dataframe to DARTS time series data type.
    series = TimeSeries.from_dataframe(df,
                                   time_col = 'Date',  
                                   value_cols = 'TotalSales',
                                   fill_missing_dates=True, freq='D')
    return series
    
    
