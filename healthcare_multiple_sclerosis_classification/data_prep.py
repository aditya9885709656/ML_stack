#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
def pre_processing(data,target_column):
    data.drop(['Unnamed: 0','Initial_EDSS', 'Final_EDSS'], axis =1, inplace = True)
    data.dropna(inplace= True)
    cat_cols = ["Gender","Breastfeeding","Varicella","Initial_Symptom","Mono_or_Polysymptomatic","Oligoclonal_Bands"]
    data = pd.get_dummies(data, columns=cat_cols,dtype=int)
    return data
    
    
