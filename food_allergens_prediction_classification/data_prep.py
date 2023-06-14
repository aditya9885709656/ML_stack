#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
def pre_processing(df):
    LE = LabelEncoder()
    df['Prediction'] = LE.fit_transform(df['Prediction'])
    #Create a new column with the frequency values for each category
    category_counts = df['Food Product'].value_counts()
    df['Food Product Freq'] = df['Food Product'].map(category_counts)
    category_counts = df['Main Ingredient'].value_counts()
    df['Main Ingredient Freq'] = df['Main Ingredient'].map(category_counts)
    category_counts = df['Sweetener'].value_counts()
    df['Sweetener Freq'] = df['Sweetener'].map(category_counts)
    category_counts = df['Fat/Oil'].value_counts()
    df['Fat/Oil Freq'] = df['Fat/Oil'].map(category_counts)
    category_counts = df['Seasoning'].value_counts()
    df['Seasoning Freq'] = df['Seasoning'].map(category_counts)
    category_counts = df['Allergens'].value_counts()
    df['Allergens Freq'] = df['Allergens'].map(category_counts)
    df = df.drop(['Food Product', 'Main Ingredient', 'Sweetener', 'Fat/Oil', 'Seasoning','Allergens'],axis=1)
    
    return df
    
    
