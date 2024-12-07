import pandas as pd

# Load the datasets
hdi_data = pd.read_csv('Processed DataSet/HDI Data v3.csv')
world_bank_data = pd.read_csv('Processed DataSet/WorldBank v2.csv')

# Filter both datasets for years from 1990 onwards
hdi_data_filtered = hdi_data[hdi_data['year'] >= 1990]
world_bank_data_filtered = world_bank_data[world_bank_data['Year'] >= 1990]

# Rename columns for consistency in joining
hdi_data_filtered = hdi_data_filtered.rename(columns={'iso3': 'Country Code', 'year': 'Year'})

# Merge HDI and World Bank datasets on 'Country Code' and 'Year'
merged_data = pd.merge(hdi_data_filtered, world_bank_data_filtered, on=['Country Code', 'Year'], how='inner')

# Display the merged data (without merging with Countries table)
print(merged_data.head())

# Save the merged HDI and World Bank dataset to a CSV file
merged_data.to_csv('Processed DataSet/Merged_HDI_WorldBank_Data v2.csv', index=False)

