import pandas as pd

df_historical_data = pd.read_csv('data/matches.csv')
df_fixture = pd.read_csv('data/fixtures.csv')
df_missing_data = pd.read_csv('data/missing.csv')

#Cleaning df_fixture
df_fixture['home'] = df_fixture['home'].str.strip()
df_fixture['away'] = df_fixture['away'].str.strip()

#Cleaning df_missing_data and adding it to df_historical_data
# df_missing_data[df_missing_data['home'].isnull()]
df_missing_data.dropna(inplace=True)
df_historical_data = pd.concat([df_historical_data, df_missing_data], ignore_index=True)
df_historical_data.drop_duplicates(inplace=True)
df_historical_data.sort_values('year', inplace=True)
#df_historical_data

#Cleaning df_historical_data

# deleting match with walk over
delete_index = df_historical_data[df_historical_data['home'].str.contains('Sweden') &
                                  df_historical_data['away'].str.contains('Austria')].index

df_historical_data.drop(index=delete_index, inplace=True)

# cleanning score and home/away columns
df_historical_data['score'] = df_historical_data['score'].str.replace('[^\d–]', '', regex=True)
df_historical_data['home'] = df_historical_data['home'].str.strip() # clean blank spaces: Yugoslavia twice
df_historical_data['away'] = df_historical_data['away'].str.strip()

# splitting score columns into home and away goals and dropping score column
df_historical_data[['HomeGoals', 'AwayGoals']] = df_historical_data['score'].str.split('–', expand=True)
df_historical_data.drop('score', axis=1, inplace=True)

# renaming columns and changing data types
df_historical_data.rename(columns={'home': 'HomeTeam', 'away': 'AwayTeam', 
                                   'year':'Year'}, inplace=True)
df_historical_data = df_historical_data.astype({'HomeGoals': int, 'AwayGoals':int, 'Year': int})

# creating new column "totalgoals"
df_historical_data['TotalGoals'] = df_historical_data['HomeGoals'] + df_historical_data['AwayGoals']


#Exporting clean dataframes

df_historical_data.to_csv('data/clean_matches.csv',index=False)

#Extra verifications

# verify number of matches per competition
years = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
         1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014,
         2018]

for year in years:
    print(year, len(df_historical_data[df_historical_data['Year']==year]))

# verify data collected for a team
print(df_historical_data[df_historical_data['HomeTeam'].str.contains('Turkey')])
print(df_historical_data[df_historical_data['AwayTeam'].str.contains('Turkey')])
    
    

