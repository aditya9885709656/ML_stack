#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
# finding artist genre used
def art_genre(df):
    for row_label in df.index:
        art_genre = np.unique(df[df['artist_code'] == df.loc[row_label,'artist_code']]['music_genre'])
        #adding art_genre column in data
        df.loc[row_label,'art_genre'] = str(art_genre)
    return df
def pre_processing(data):
    le = LabelEncoder()
    data.drop(data[data['tempo'] == '?'].index , inplace = True)
    data["tempo"] = data["tempo"].astype(float)
    #converting ms to seconds
    data["duration_ms"]=data["duration_ms"]/1000
    data['popularity']=data['popularity']/100
    data.dropna(how='any', inplace=True)
    #dropping track_name since music_genre is independent on track_name
    data.drop(['track_name'],axis=1,inplace=True)
    data['key']=le.fit_transform(data['key'])
    data['mode']=le.fit_transform(data['mode'])
    data['obtained_date']=le.fit_transform(data['obtained_date'])
    data['artist_code'] = le.fit_transform(data['artist_name'])
    data['music_genre'] = le.fit_transform(data['music_genre'])
    #Label encoding class: {'Alternative': 0, 'Anime': 1, 'Blues': 2, 'Classical': 3, 'Country': 4, 'Electronic': 5, 'Hip-Hop': 6, 'Jazz': 7, 'Rap': 8, 'Rock': 9}
    data['art_genre'] = le.fit_transform(data['art_genre'])
    data.drop(['instance_id','key','tempo','artist_code','artist_name','liveness','duration_ms','obtained_date','energy'],axis=1,inplace=True)
    
    return data
    
    
