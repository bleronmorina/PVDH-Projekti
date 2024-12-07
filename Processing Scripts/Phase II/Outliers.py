import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore
from sklearn.ensemble import IsolationForest

# Load the dataset
file_path = 'Processed DataSet/Phase II/Modified_Dataset.csv'  # Replace with your file path
df = pd.read_csv(file_path)

# Select only numerical columns for outlier detection
numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
numerical_data = df[numerical_cols]
numerical_data = numerical_data.drop(columns=['GDP (USD)'], errors='ignore')  # Ignore GDP column

# Step 1: Z-Score Method
z_scores = np.abs(zscore(numerical_data, nan_policy='omit'))
z_threshold = 100 
outliers_zscore = (z_scores > z_threshold).any(axis=1)

# Step 2: Interquartile Range (IQR) Method
Q1 = numerical_data.quantile(0.25)
Q3 = numerical_data.quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 60 * IQR 
upper_bound = Q3 + 60 * IQR
outliers_iqr = ((numerical_data < lower_bound) | (numerical_data > upper_bound)).any(axis=1)

# Step 3: Isolation Forest (Machine Learning Approach)
iso_forest = IsolationForest(contamination=0.0000002, random_state=42)  # Reduced contamination rate
outlier_pred = iso_forest.fit_predict(numerical_data.fillna(0))  # Filling NaN values temporarily
outliers_iso = outlier_pred == -1

# Combine Results from All Methods
combined_outliers = outliers_zscore | outliers_iqr | outliers_iso

# Analyze Results
outlier_counts = {
    'Z-Score Method': outliers_zscore.sum(),
    'IQR Method': outliers_iqr.sum(),
    'Isolation Forest': outliers_iso.sum(),
    'Combined': combined_outliers.sum()
}

# Visualize Outliers
plt.figure(figsize=(12, 8))
sns.boxplot(data=numerical_data, orient='h', palette='Set2')
plt.title("Boxplot of Numerical Features to Visualize Potential Outliers")
plt.show()

# Save the outliers to a new CSV file
outliers_df = df[combined_outliers]
outliers_df.to_csv('Processed DataSet/Phase II/Detected_Outliers.csv', index=False)

# Summary
print("Outlier Detection Summary:")
print(outlier_counts)
print(f"Total rows flagged as outliers: {combined_outliers.sum()} out of {len(df)}")

# Save dataset without outliers
cleaned_df = df[~combined_outliers]
cleaned_df.to_csv('Processed DataSet/Phase II/Cleaned_Data.csv', index=False)

print("Outliers have been saved to 'Processed DataSet/Phase II/Detected_Outliers.csv'.")
print("Cleaned dataset has been saved to 'Processed DataSet/Phase II/Cleaned_Data.csv'.")
