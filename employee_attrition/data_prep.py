#Import necessary libraries
import pandas as pd
import numpy as np
def pre_processing(data):
    #Converting to date data type
    data['Dateofjoining'] = pd.to_datetime(data['Dateofjoining'])
    data['LastWorkingDate'] = pd.to_datetime(data['LastWorkingDate'])
    #Creating necessary new columns
    data['Year_of_join'] = data['Dateofjoining'].apply(lambda t:t.year)
    data['Month_of_join'] = data['Dateofjoining'].apply(lambda t:t.month)
    data['Day_of_join'] = data['Dateofjoining'].apply(lambda t:t.day)
    data['Year_of_leave'] = data['LastWorkingDate'].apply(lambda t:t.year)
    data['Month_of_leave'] = data['LastWorkingDate'].apply(lambda t:t.month)
    data = data.astype({'Year_of_join':int,'Month_of_join':int,'Day_of_join':int})
    data.drop(columns='Dateofjoining',inplace=True)
    #Create Attrition column
    data['Attrition'] = np.nan
    #Alligning columns
    pop_col = data.pop('Attrition')
    data.insert(1,'Attrition',pop_col)
    pop_col = data.pop('Year_of_join')
    data.insert(8,'Year_of_join',pop_col)
    pop_col = data.pop('Month_of_join')
    data.insert(9,'Month_of_join',pop_col)
    pop_col = data.pop('Day_of_join')
    data.insert(10,'Day_of_join',pop_col)
    data['Attrition']=np.where(data['LastWorkingDate'].isnull(),0,1)
    data.drop(columns='LastWorkingDate',inplace=True)
    data['Length_of_work'] = data['Year_of_leave'] - data['Year_of_join']
    sex = pd.get_dummies(data['Gender'])
    city = pd.get_dummies(data['City'])
    edu = pd.get_dummies(data['Education_Level'])
    data.drop(columns=['MMM-YY','Emp_ID','Gender','City','Education_Level','Joining Designation','Designation','Year_of_leave','Month_of_leave','Length_of_work'],inplace=True)
    data = pd.concat([data,sex,city,edu],axis=1)
    return data
    
    
