#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
# function to removes outliers
def remove_outliers(data):
    q1 = np.percentile(data,25)
    q3 = np.percentile(data,75)
    iqr = q3-q1
    upper = q3+1.5*iqr
    lower = q1-1.5*iqr
    data[(data>lower)&(data<upper)]
    return data[(data>lower)&(data<upper)]
def pre_processing(df):
    # create an empty data frame
    df_clean = pd.DataFrame()
    # populate data frame with no outliers
    for name,value in df.iteritems():
        df_clean[name] = remove_outliers(value)
    # remove missing values
    df_clean.dropna(axis=0,inplace=True)

    # reset index
    df_clean.reset_index(drop=True, inplace=True)
    return df_clean
    
    
