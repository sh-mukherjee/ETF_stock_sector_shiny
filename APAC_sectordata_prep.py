import yfinance as yf
import pandas as pd

# Get the ETF tickers of the MSCI Index ETFs for the countries Taiwan, Japan, South Korea, Singapore and Hong Kong
ticker_tw = yf.Ticker("EWT")
ticker_jp = yf.Ticker("EWJ")
ticker_kr = yf.Ticker("EWY")
ticker_sg = yf.Ticker('EWS')
ticker_hk = yf.Ticker('EWH')

# Get the ETF info
info_tw = ticker_tw.info
info_jp = ticker_jp.info
info_kr = ticker_kr.info
info_sg = ticker_sg.info
info_hk = ticker_hk.info

# ---------------------------------------------------------
################ TAIWAN ##################
#Taiwan - List of dictionaries to merge
dict_list_tw = info_tw['sectorWeightings']

# Create an empty dictionary to store the merged dictionaries
merged_dict_tw = {}

# Iterate through the list of dictionaries
for dictionary in dict_list_tw:
    # Use the update() method to add the key-value pairs from each dictionary to the merged dictionary
    merged_dict_tw.update(dictionary)

# The merged dictionary now contains the key-value pairs from all of the dictionaries in the list
print(merged_dict_tw)  # Output: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

################# JAPAN #####################
# Japan - List of dictionaries to merge
dict_list_jp = info_jp['sectorWeightings']

# Create an empty dictionary to store the merged dictionaries
merged_dict_jp = {}

# Iterate through the list of dictionaries
for dictionary in dict_list_jp:
    # Use the update() method to add the key-value pairs from each dictionary to the merged dictionary
    merged_dict_jp.update(dictionary)

# The merged dictionary now contains the key-value pairs from all of the dictionaries in the list
print(merged_dict_jp)  # Output: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

#################### KOREA ####################
# Korea - List of dictionaries to merge
dict_list_kr = info_kr['sectorWeightings']

# Create an empty dictionary to store the merged dictionaries
merged_dict_kr = {}

# Iterate through the list of dictionaries
for dictionary in dict_list_kr:
    # Use the update() method to add the key-value pairs from each dictionary to the merged dictionary
    merged_dict_kr.update(dictionary)

# The merged dictionary now contains the key-value pairs from all of the dictionaries in the list
print(merged_dict_kr)  # Output: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

################# SINGAPORE ####################
# Singapore - List of dictionaries to merge
dict_list_sg = info_sg['sectorWeightings']

# Create an empty dictionary to store the merged dictionaries
merged_dict_sg = {}

# Iterate through the list of dictionaries
for dictionary in dict_list_sg:
    # Use the update() method to add the key-value pairs from each dictionary to the merged dictionary
    merged_dict_sg.update(dictionary)

# The merged dictionary now contains the key-value pairs from all of the dictionaries in the list
print(merged_dict_sg)  # Output: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

################### HONG KONG ####################
# Hong Kong - List of dictionaries to merge
dict_list_hk = info_hk['sectorWeightings']

# Create an empty dictionary to store the merged dictionaries
merged_dict_hk = {}

# Iterate through the list of dictionaries
for dictionary in dict_list_hk:
    # Use the update() method to add the key-value pairs from each dictionary to the merged dictionary
    merged_dict_hk.update(dictionary)

# The merged dictionary now contains the key-value pairs from all of the dictionaries in the list
print(merged_dict_hk)  # Output: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# ------------------------------------------------------------

# creat a Dataframe object from a list of tuples of key, value pair
df_tw = pd.DataFrame(list(merged_dict_tw.items()),columns=['Sector', 'Weight'])
df_jp = pd.DataFrame(list(merged_dict_jp.items()),columns=['Sector', 'Weight'])
df_kr = pd.DataFrame(list(merged_dict_kr.items()),columns=['Sector', 'Weight'])
df_sg = pd.DataFrame(list(merged_dict_sg.items()),columns=['Sector', 'Weight'])
df_hk = pd.DataFrame(list(merged_dict_hk.items()),columns=['Sector', 'Weight'])

# Add a column with the name of the country
df_tw['Country'] = 'Taiwan'
df_jp['Country'] = 'Japan'
df_kr['Country'] = 'Korea'
df_sg['Country'] = 'Singapore'
df_hk['Country'] = 'Hong Kong'

# Combine all the country dataframes into one big dataframe
df = pd.concat([df_tw,df_jp,df_kr,df_sg,df_hk],ignore_index=True)

# We will multiply each value in the column 'Weight' by 100 to make it a percentage
df['Weight'] = df['Weight'].multiply(100)
df.rename(columns={'Weight':'Weight(%)'}, inplace=True)
print(df)

# get a list of unique values in the 'Sector' column of the dataframe
sector_list = df['Sector'].unique().tolist()
print(sector_list)

# dictionary with keys equal to the elements of the sectors and values as specified in the assignment
sector_dict = {'realestate': 'Real Estate', 'consumer_cyclical': 'Consumer Cyclical', 'basic_materials': 'Basic Materials', 'consumer_defensive': 'Consumer Defensive', 'technology': 'Technology', 'communication_services': 'Communication Services', 'financial_services': 'Financial Services', 'utilities': 'Utilities', 'industrials': 'Industrials', 'energy': 'Energy', 'healthcare': 'Healthcare'}

# create a new column in the dataframe caled 'Sector_Name' and fill it with the values from the sector_dict
df['Sector_Name'] = df['Sector'].map(sector_dict)
print(df)

# write the dataframe to a csv file with index set to false
df.to_csv('APAC_sector_weight1.csv', index=False)