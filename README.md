# FIFA 2022 World Cup Winner Prediction
This repository contains the code to scrape FIFA World Cup matches since 1930 and up to 2022, clean the data and use it to train a machine learning model for predicting match outcomes.

Scraping
The code for scraping is in the file scraping.py and is split into two parts:

get_matches(year): This function takes a year (e.g., 1930) and scrapes the FIFA World Cup matches for that year from the corresponding Wikipedia page. It returns a Pandas DataFrame with the home team, away team, and score for each match.

get_missing_data(year): This function takes a year and scrapes the matches that are missing from the corresponding Wikipedia page using Selenium. This is necessary because the format of the tables on the pages is not consistent. The function returns a Pandas DataFrame with the home team, away team, and score for each match.

The scraped data is stored in CSV files for historical matches, 2022 fixtures, and missing matches.

Cleaning
The code for cleaning the scraped data is in the file cleaning.py. The steps performed are:

Load the historical matches, 2022 fixtures, and missing matches CSV files as Pandas DataFrames.

Clean the df_fixture DataFrame by removing leading and trailing white spaces in the home and away team names.

Clean the df_missing_data DataFrame by dropping any rows with missing data, and add it to df_historical_data.

Delete the match between Sweden and Austria in the 1958 World Cup because it was a walkover.

Clean the home and away team names and the score in df_historical_data.

Split the score into the number of goals scored by the home team and the away team.

Rename columns and change data types as necessary.

Create a new column for the total number of goals in each match.

Export the cleaned data as a CSV file.

Prediction
The code for predicting the outcomes of 2022 World Cup matches is in the file prediction.py. It uses the cleaned historical data to train a Random Forest Classifier model and predicts the outcomes of the 2022 fixtures. The predicted outcomes are stored in a Pandas DataFrame and exported to a CSV file.

Conclusion
This repository contains the code for scraping, cleaning, and predicting FIFA World Cup matches. The scraped data is cleaned and used to train a machine learning model that predicts the outcomes of 2022 World Cup matches. The code can be used as a starting point for further analysis and prediction of football matches.
