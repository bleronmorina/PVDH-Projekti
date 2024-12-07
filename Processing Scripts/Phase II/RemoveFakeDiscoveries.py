import pandas as pd

# Load the dataset
data = pd.read_csv("Merged_HDI_WorldBank_Data v3.csv")


# 2. Handle missing values
# Replace missing numerical values with the column mean
data_cleaned = data.fillna(data.mean(numeric_only=True))

# Replace missing categorical values (if any) with the mode
for column in data.select_dtypes(include=['object']).columns:
    data_cleaned[column].fillna(data_cleaned[column].mode()[0], inplace=True)

# 3. Remove duplicates
data_cleaned = data_cleaned.drop_duplicates()

# 4. Save the cleaned dataset
data_cleaned.to_csv("Removed_Fake_Discoveries.csv", index=False)

print("Cleaning process completed. Cleaned dataset saved as 'cleaned_dataset.csv'.")

