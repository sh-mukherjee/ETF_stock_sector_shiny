import yfinance as yf
import pandas as pd

tickers = ['EWA', 'EWH', 'EWJ', 'EWM', 'EWS', 'EWT', 'EWY', 'THD']
countries = ['Australia', 'Hong Kong', 'Japan', 'Malaysia', 'Singapore', 'Taiwan', 'South Korea', 'Thailand']

all_dataframes = []

for ticker, country in zip(tickers, countries):
    ticker_data = yf.Ticker(ticker)
    info = ticker_data.info

    # Extract the list of dictionaries for sector weightings
    dict_list = info['sectorWeightings']

    # Create an empty dictionary to store the merged dictionaries
    merged_dict = {}

    # Iterate through the list of dictionaries
    for dictionary in dict_list:
        # Use the update() method to add the key-value pairs from each dictionary to the merged dictionary
        merged_dict.update(dictionary)

    # Create a Dataframe object from a list of tuples of key, value pair
    df = pd.DataFrame(list(merged_dict.items()), columns=['Sector', 'Weight'])
    
    # Add the Country column
    df['Country'] = country
    
    # Append the dataframe to the list
    all_dataframes.append(df)

# Concatenate all dataframes into one
final_df = pd.concat(all_dataframes, ignore_index=True)

# Display the final dataframe
print(final_df)