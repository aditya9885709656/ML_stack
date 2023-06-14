#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
def pre_processing(data):
    data['price_cad'] = data['price_cad'].apply(lambda x:str(x).strip().replace('$','')).astype(float)
    data['diameter'] = data['diameter'].str.replace(' inch','').str.replace(' \n','').astype(float)
    data.loc[:,data.dtypes=='object'] = data.select_dtypes(include=['object']).apply(lambda x:x.astype('category'))
    columns = ['company', 'topping', 'variant', 'size', 'extra_sauce', 'extra_cheese','extra_mushrooms']
    data1 = pd.concat([data]+[pd.get_dummies(data[i],drop_first=True) for i in columns],axis=1)
    data1.drop(columns,axis=1,inplace=True)
    return data1
    
    
