import pandas as pd
from scipy import stats
import numpy as np

# Load the dataset
file_path = 'C:/Users/blero/Git-Repo/PVDH-Projekti/Unprocessed DataSet/WorldBank.csv'  # Replace with your CSV file path
df = pd.read_csv(file_path)

# Calculate missing data as a percentage per column
missing_data_percentage = df.isnull().mean() * 100
missing_data_percentage = missing_data_percentage[missing_data_percentage > 0]

# Check for negative values in columns where negative values may not make sense
# Define columns where negative values are logically invalid
invalid_negative_columns = []  # Fill in columns manually based on your dataset knowledge

# Automatically detect columns where negative values may not make sense (optional)
# You might want to manually add more column names to 'invalid_negative_columns' if needed.
# For example, only consider numerical columns with names that suggest counts, measurements, etc.
for column in df.select_dtypes(include=['number']).columns:
    if column.lower().startswith(('age', 'population', 'income', 'gdp', 'count', 'number', 'rate')):
        invalid_negative_columns.append(column)

# Check for negative values
negative_data_counts = {}
for column in invalid_negative_columns:
    negative_count = (df[column] < 0).sum()
    if negative_count > 0:
        negative_data_counts[column] = negative_count / len(df) * 100  # Percentage of negative values

# Display results
print("Missing Data Percentage per Column:")
print(missing_data_percentage)

print("\nColumns with Invalid Negative Values (as percentage of total):")
for column, percentage in negative_data_counts.items():
    print(f"{column}: {percentage:.2f}%")
