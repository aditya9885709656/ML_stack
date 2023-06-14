#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
def pre_processing(data):
    # Changing data types to correct ones
    data["date"] = pd.to_datetime(data["date"])
    data = data.replace({'shoot_out': {'Yes': True, 'No': False}})
    world_cup_teams = ['Qatar', 'Netherlands', 'Senegal', 'Ecuador', 'England', 'USA', 'IR Iran', 'Wales',
                   'Argentina', 'Mexico', 'Poland', 'Saudi Arabia', 'France', 'Denmark', 'Tunisia', 'Australia',
                   'Spain', 'Germany', 'Japan', 'Costa Rica', 'Belgium', 'Croatia', 'Morocco', 'Canada',
                   'Brazil', 'Switzerland', 'Serbia', 'Cameroon', 'Portugal', 'Uruguay', 'Korea Republic', 'Ghana']
    # Removing irrelevant matches
    # Keep matches between teams of World Cup, their matches with teams that have ranking less than 100
    # Keep matches between teams with ranking less than 50

    data = data[((data['home_team'].isin(world_cup_teams) & data['away_team'].isin(world_cup_teams)) |
                       (data['home_team'].isin(world_cup_teams) & (data['away_team_fifa_rank'] <= 100)) |
                       ((data['home_team_fifa_rank'] <= 100) & data['away_team'].isin(world_cup_teams))|
                       ((data['home_team_fifa_rank'] <= 50) & (data['away_team_fifa_rank'] <= 50)))]
    data.reset_index(drop=True, inplace=True)
    # Creating features for training
    data["goal_difference"] = data["home_team_score"] - data["away_team_score"]
    data["rank_difference"] = data["home_team_fifa_rank"] - data["away_team_fifa_rank"]
    data['Friendly'] = data['tournament'] == 'Friendly'
    data['year'] = data['date'].dt.year
    
    return data
    
    
