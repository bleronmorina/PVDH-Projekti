import pandas as pd

# Load the dataset
file_path = '../../Unprocessed DataSet/HDI.csv'
data = pd.read_csv(file_path)

# Exclude regional aggregates if necessary
exclude_regions = [
    'World', 'Very high human development', 'Low human development', 
    'Medium human development', 'High human development', 
    'Sub-Saharan Africa', 'Europe and Central Asia', 'South Asia',
    'Latin America and the Caribbean', 'East Asia and the Pacific', 'Arab States'
]
data = data[~data['country'].isin(exclude_regions)]

# Identify columns that represent year-specific data
year_columns = [col for col in data.columns if any(str(year) in col for year in range(1900, 2100))]

# Reshape the dataset to long format
reshaped_data = data.melt(
    id_vars=[col for col in data.columns if col not in year_columns],  # Non-year columns remain as identifiers
    value_vars=year_columns,  # Columns to unpivot
    var_name='indicator',     # New column to indicate the type of indicator (e.g., 'hdi_1990')
    value_name='value'        # Values from the unpivoted columns
)

# Extract the year from the indicator column
reshaped_data['year'] = reshaped_data['indicator'].str.extract(r'(\d{4})').astype(float)  # Use float temporarily
missing_years = reshaped_data[reshaped_data['year'].isnull()]
print(f"Rows with missing years: {missing_years}")

# Continue processing only valid years
reshaped_data = reshaped_data.dropna(subset=['year'])
reshaped_data['year'] = reshaped_data['year'].astype(int)

# Extract the base indicator name (e.g., 'hdi' from 'hdi_1990')
reshaped_data['indicator'] = reshaped_data['indicator'].str.extract(r'^(.*?)(?:_\d{4})?$')

# Check year-specific data for missing countries
missing_countries = set(data['country']) - set(reshaped_data['country'])
missing_year_data = data.loc[data['country'].isin(missing_countries), year_columns]
print(f"Missing year data:\n{missing_year_data}")

# Ensure no rows are dropped unnecessarily during pivoting
reshaped_data = reshaped_data.fillna(0)

# Pivot the data
final_data = reshaped_data.pivot_table(
    index=['iso3', 'country', 'region', 'year'],
    columns='indicator',
    values='value',
    aggfunc='first'
).reset_index()

# Check missing countries again after pivoting
final_countries = set(final_data['country'])
remaining_missing = set(data['country']) - final_countries
print(f"Remaining missing countries after pivoting: {remaining_missing}")

output_path = '../../Processed DataSet/Phase I/HDI Data v1.csv'
final_data.to_csv(output_path, index=False)

# Display the first few rows of the reshaped dataset
final_data.head()
