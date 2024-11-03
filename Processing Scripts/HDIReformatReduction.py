import pandas as pd

# Load the dataset
file_path = '/Unprocessed DataSet/HDI.csv'
data = pd.read_csv(file_path)

# Melt the dataframe so that each year-indicator pair becomes a separate row
melted_data = pd.melt(data,
                      id_vars=['iso3', 'country', 'hdicode', 'region', 'hdi_rank_2021'],
                      var_name='indicator_year',
                      value_name='value')

# Extract the indicator and year from the 'indicator_year' column
melted_data[['indicator', 'year']] = melted_data['indicator_year'].str.extract(r'([a-zA-Z_]+)_(\d{4})')
melted_data['year'] = melted_data['year'].astype(float)  # Convert year to float for proper sorting

# Drop the original 'indicator_year' column
melted_data = melted_data.drop(columns=['indicator_year'])

# Pivot the table so that each indicator becomes a column, with year as a separate column
reshaped_data = melted_data.pivot_table(index=['iso3', 'country', 'hdicode', 'region', 'hdi_rank_2021', 'year'],
                                        columns='indicator',
                                        values='value').reset_index()

# Save the transformed dataset to a new CSV file
output_path = '/Processed DataSet/HDI Data v1.csv'
reshaped_data.to_csv(output_path, index=False)
