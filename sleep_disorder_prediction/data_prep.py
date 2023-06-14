#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
def pre_processing(data):
    # Combining both Doctor and Nurse due to how similiar they are
    data['Occupation'] = data['Occupation'].replace(['Doctor', 'Nurse'], 'Healthcare')
    le = LabelEncoder()
    data['BMI Category'] = le.fit_transform(data['BMI Category'])
    data['Gender'] = le.fit_transform(data['Gender'])
    data = pd.get_dummies(data, columns=['Occupation'])
    data[['Systolic_BP', 'Diastolic_BP']] = data['Blood Pressure'].str.split('/', expand=True)
    data['Systolic_BP'] = pd.to_numeric(data['Systolic_BP'])
    data['Diastolic_BP'] = pd.to_numeric(data['Diastolic_BP'])
    data = data.drop(columns='Blood Pressure') 
    return data
    
    
