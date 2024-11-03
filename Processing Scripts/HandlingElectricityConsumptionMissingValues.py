import pandas as pd

# Load both datasets
merged_hdi = pd.read_csv('WorldBank v2.csv')
electricity_consumption = pd.read_csv('Electricity_Consumption_First_Table.csv')
print(electricity_consumption.columns)

# Rename columns for consistency
electricity_consumption = electricity_consumption.rename(columns={'Country Code': 'Country Code', 'Consumption per capita kWh/yr': 'Electricity Consumption'})

# Merge the datasets on 'Country'
merged_data = pd.merge(merged_hdi, electricity_consumption[['Country Code', 'Electricity Consumption']], 
                       on='Country Code', how='left')

# Target column for filling
target_col = 'Electric power consumption (kWh per capita)'

# Fill missing values in the target column linearly based on a 5% decrement of 'Electricity Consumption'
for country in merged_data['Country Code'].unique():
    country_data = merged_data[merged_data['Country Code'] == country]
    electricity_value = country_data['Electricity Consumption'].iloc[0]
    
    if pd.notna(electricity_value):
        years = country_data['Year'].sort_values(ascending=False).reset_index(drop=True)
        for i, year in enumerate(years):
            idx = country_data[country_data['Year'] == year].index
            adjusted_value = electricity_value * (0.97 ** i)  # Reduce by 5% each year
            merged_data.loc[idx, target_col] = adjusted_value

# Drop the helper column and save the result
merged_data = merged_data.drop(columns=['Electricity Consumption'])
merged_data.to_csv('WorldBank v3.csv', index=False)
