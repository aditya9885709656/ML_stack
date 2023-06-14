#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.preprocessing import OneHotEncoder
def pre_processing(data):
    encoder = OrdinalEncoder()
    mask = data.isin(['?'])
    data = data[~mask.any(axis=1)]
    data['age'] = pd.to_numeric(data['age'], errors='coerce')
    data['age_bin'] = pd.cut(data['age'], bins=[0, 12, 18, 65, 120],labels=['Child', 'Teenager', 'Adult', 'Elderly'])
    data[['age_bin']] = encoder.fit_transform(data[['age_bin']])
    scaler = MinMaxScaler()
    numerical_cols = ['erythema', 'scaling', 'exocytosis', 'acanthosis', 'hyperkeratosis']
    data[numerical_cols] = scaler.fit_transform(data[numerical_cols])
    # Feature Aggregation
    aggregated_features = data[['erythema', 'scaling', 'exocytosis']].mean(axis=1)
    data['aggregated_features'] = aggregated_features
    # Domain-Specific Transformations
    data['log_erythema'] = np.log1p(data['erythema'])
    data['scaling_squared'] = data['scaling'] ** 2
    return data
    
    
