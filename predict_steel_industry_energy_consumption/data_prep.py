#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
def pre_processing(data):
    #Rename column names
    data = data.rename(columns={'Lagging_Current_Reactive.Power_kVarh': 'Lagging_Reactive_Power_kVarh',
                        'Leading_Current_Reactive_Power_kVarh': 'Leading_Reactive_Power_kVarh',
                        'Lagging_Current_Power_Factor': 'Lagging_Power_Factor',
                        'Leading_Current_Power_Factor': 'Leading_Power_Factor',
                        'CO2(tCO2)':'CO2'})
    categ = data.select_dtypes(include = "object").columns
    le = LabelEncoder()
    data[categ] = data[categ].apply(le.fit_transform)
    return data
    
    
