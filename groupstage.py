import pandas as pd
import pickle
from string import ascii_uppercase as alphabet

# extracting all tables in website
all_tables = pd.read_html('https://en.wikipedia.org/wiki/2022_FIFA_World_Cup')
# A -> H
# 11 -> 7*8 + 11 = 67

#Assigning pos numbers to numbers i.e groupstage and putting them in a dictionary
dict_table = {}
for letter, i in zip(alphabet, range(11,67,7)): # A=11, B=18, ...
    df = all_tables[i]
    df.rename(columns={df.columns[1]:'Team'}, inplace=True)
    df.pop('Qualification')
    dict_table[f'Group {letter}'] = df
     
#dict_table.keys() - prints all groups with assigned letters

with open('dict_table', 'wb') as output:
    pickle.dump(dict_table, output)