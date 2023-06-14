#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
def pre_processing(df):
    df.rename(columns = {'Day.Of.Week':'day_of_week'
                    ,'Page.Loads':'page_loads'
                    ,'Unique.Visits':'unique_visits'
                    ,'First.Time.Visits':'first_visits'
                    ,'Returning.Visits':'returning_visits'}, inplace = True)
    df=df.replace(',','',regex=True)
    df['page_loads']=df['page_loads'].astype(int)
    df['unique_visits']=df['unique_visits'].astype(int)
    df['first_visits']=df['first_visits'].astype(int)
    df['returning_visits']=df['returning_visits'].astype(int)
    pred_df=df[['page_loads' ,'unique_visits' ,'first_visits' ,'returning_visits','Day']]
    #Tuesday, wednesday, thursday and monday are the days when our website received the most traffic so we will create a feature days_f of them 1 value will define their existence and 0 will define the rest of the days.
    pred_df['days_f']=np.where((df['Day']=='Tuesday') | 
                      (df['Day']=='Wednesday') | 
                      (df['Day']=='Thursday') |
                      (df['Day']=='Monday'),1,0)
    pred_df.drop('Day',axis=1,inplace=True)
    return pred_df
    
    
