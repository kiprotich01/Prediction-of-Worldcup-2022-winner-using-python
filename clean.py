import pandas as pd

df_historical_data = pd.read_csv('fifa_worldcup_matches.csv')
df_fixture = pd.read_csv('fifa_worldcup_fixtures.csv')
df_missing_data = pd.read_csv('fifa_worldcup_missing_data.csv')

#Cleaning df_fixture
df_fixture['home'] = df_fixture['home'].str.strip()
df_fixture['away'] = df_fixture['away'].str.strip()

