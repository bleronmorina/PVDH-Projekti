import pandas as pd

# Load the dataset (adjust file path as necessary)
data = pd.read_csv('/Unprocessed DataSet/HDI.csv')

# List of columns to remove
columns_to_remove = ['loss', 'hdi_rank', 'gii_rank', 'gdi', 'gdi_group', 'rankdiff_hdi_phdi']

# Remove the specified columns if they exist in the dataset
data = data.drop(columns=[col for col in columns_to_remove if col in data.columns])

# Save the modified dataset (adjust file path as necessary)
data.to_csv('/Processed DataSet/HDI Data v2.csv', index=False)

