import yahooquery as yq
import pandas as pd

tickers = ['EWA', 'EWH', 'EWJ', 'EWM', 'EWS', 'EWT', 'EWY', 'THD']
countries = ['Australia', 'Hong Kong', 'Japan', 'Malaysia', 'Singapore', 'Taiwan', 'South Korea', 'Thailand']


all_dataframes = []

for ticker, country in zip(tickers, countries):
    t = yq.Ticker(ticker)
    # sector weightings, returns pandas DataFrame with one column containing the weights, indexed by the sector names
    df = t.fund_sector_weightings
    # give a name to the first column
    df.columns = ['Weight']
    # turn the index column into a dataframe column
    df['Sector'] = df.index
    
    # Add the Country column
    df['Country'] = country
    
    # Append the dataframe to the list
    all_dataframes.append(df)

# Concatenate all dataframes into one
sector_df = pd.concat(all_dataframes, ignore_index=True)

# dictionary with keys equal to the elements of the sectors and values as specified in the assignment
sector_dict = {'realestate': 'Real Estate', 'consumer_cyclical': 'Consumer Cyclical', 'basic_materials': 'Basic Materials', 'consumer_defensive': 'Consumer Defensive', 'technology': 'Technology', 'communication_services': 'Communication Services', 'financial_services': 'Financial Services', 'utilities': 'Utilities', 'industrials': 'Industrials', 'energy': 'Energy', 'healthcare': 'Healthcare'}

# create a new column in the dataframe caled 'Sector_Name' and fill it with the values from the sector_dict
sector_df['Sector_Name'] = sector_df['Sector'].map(sector_dict)

# Reorder the columns
new_order = ['Country', 'Sector_Name', 'Weight', 'Sector']
sector_df = sector_df[new_order]

# Drop the 'Sector' column
sector_df = sector_df.drop('Sector', axis=1)

# Convert 'Weight' column to percentages
sector_df['Weight'] = sector_df['Weight'] * 100
# Rename the 'Weight' column
sector_df = sector_df.rename(columns={'Weight': 'Weight(%)'})
