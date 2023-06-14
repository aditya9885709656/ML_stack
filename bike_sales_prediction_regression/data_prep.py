#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
def pre_processing(data):
    # The variable instant is just a record index and not useful for prediction, Hence dropped
    data = data.drop('instant',axis=1)
    # The variable atemp is just a derivative of temp variable(inferred from data dictionary) and is highly correlated, Hence dropped
    data = data.drop('atemp',axis=1)
    # The variable dteday is not useful since we have year and month variables separately, Hence dropped
    data = data.drop('dteday',axis=1)
    # The variables casual and registered are subsets of cnt(target variable), Hence they are highly correlated and thus dropped
    data = data.drop(['casual','registered'],axis=1)
    # season : season (1:spring, 2:summer, 3:fall, 4:winter)
    # Mapping the season names accordingly in the data
    data['season'] = data['season'].map({1:"spring",2:"summer",3:"fall",4:"winter"})

    # mnth : month ( 1 to 12)
    # Mapping the month names accordingly in the data
    data['mnth'] = data['mnth'].map({1: "jan",2: "feb",3: "mar",4: "apr",5: "may",6: "jun",7: "jul",8: "aug",9: "sep",10: "oct" ,11: "nov" ,12: "dec"})

    # weekday : day of the week
    # The weekdays are mapped with the numbers from ( 0:"sunday"------6:"saturday")
    data['weekday'] = data['weekday'].map({0: "sun",1: "mon",2: "tue",3: "wed",4: "thu",5: "fri",6: "sat"})

    # weathersit -- 1:"clear",2:"cloudy",3:"light_rain",4:"heavy_rain"
    data['weathersit'] = data['weathersit'].map({1:"clear",2:"cloudy",3:"light_rain",4:"heavy_rain"})
    # Creating dummy variables for the categories ('season','mnth','weekday','weathersit')
    data = pd.get_dummies(data=data,columns=["season","mnth","weekday"],drop_first=True)
    data = pd.get_dummies(data=data,columns=["weathersit"])
    
    return data
    
    
