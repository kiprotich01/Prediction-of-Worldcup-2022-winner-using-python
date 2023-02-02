import pandas as pd
import pickle
from scipy.stats import poisson
dict_table = pickle.load(open('data/dict_table','rb'))
df_historical_data = pd.read_csv('data/clean_matches.csv')
df_fixture = pd.read_csv('data/clean_fixture.csv')

#Calculate Team Strength

df_home = df_historical_data[['HomeTeam', 'HomeGoals', 'AwayGoals']]
df_away = df_historical_data[['AwayTeam', 'HomeGoals', 'AwayGoals']]

df_home = df_home.rename(columns={'HomeTeam':'Team', 'HomeGoals': 'GoalsScored', 'AwayGoals': 'GoalsConceded'})
df_away = df_away.rename(columns={'AwayTeam':'Team', 'HomeGoals': 'GoalsConceded', 'AwayGoals': 'GoalsScored'})

df_team_strength = pd.concat([df_home, df_away], ignore_index=True).groupby(['Team']).mean()
df_team_strength

