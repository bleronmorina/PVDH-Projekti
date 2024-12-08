import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# **Load the Dataset**
file_path = '../../Processed DataSet/Phase I/Merged_HDI_WorldBank_Data v3.csv'

try:
    data = pd.read_csv(file_path)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print(f"Error: Dataset not found at {file_path}. Check the file path.")
    exit()

# **Helper Functions**

def display_statistics():
    """Show key statistics."""
    print("\nSummary Statistics (Numerical Columns):")
    print(data.describe())
    print("\nMissing Values in Each Column:")
    missing_values = data.isnull().sum()
    print(missing_values[missing_values > 0])

def plot_missing_values():
    """Visualize missing values."""
    plt.figure(figsize=(10, 6))
    sns.heatmap(data.isnull(), cbar=False, cmap="viridis")
    plt.title("Missing Values in the Dataset")
    plt.show()

def plot_correlation():
    """Plot the correlation matrix for numerical data."""
    numeric_data = data.select_dtypes(include=['number'])
    correlation_matrix = numeric_data.corr()

    # Display correlation matrix
    print("\nCorrelation Matrix (Top 5 Relationships):")
    print(correlation_matrix.unstack().sort_values(key=lambda x: abs(x), ascending=False)[1:6])

    # Visualize the correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=False, cmap="coolwarm", cbar=True, square=True)
    plt.title("Correlation Matrix (Simplified)")
    plt.show()

def plot_pairwise_relationships():
    """Plot pairwise relationships for key columns."""
    columns_to_plot = ['HDI', 'GDP per capita (USD)', 'Life expectancy at birth (years)', 
                       'Individuals using the Internet (%)']
    available_columns = [col for col in columns_to_plot if col in data.columns]
    
    if available_columns:
        sns.pairplot(data[available_columns])
        plt.suptitle("Pairwise Relationships for Key Variables", y=1.02)
        plt.show()
    else:
        print("Key columns for pairwise relationships are not present in the dataset.")

def plot_distributions():
    """Plot distributions of key numerical columns."""
    columns_to_plot = ['HDI', 'GDP per capita (USD)', 'Life expectancy at birth (years)', 
                       'Individuals using the Internet (%)']
    for column in columns_to_plot:
        if column in data.columns:
            sns.histplot(data[column].dropna(), kde=True, bins=30, color='blue')
            plt.title(f"Distribution of {column}")
            plt.xlabel(column)
            plt.ylabel("Frequency")
            plt.show()

def plot_relationships():
    """Analyze relationships between HDI and GDP per capita."""
    if 'GDP per capita (USD)' in data.columns and 'HDI' in data.columns:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=data, x='GDP per capita (USD)', y='HDI', hue='Region', palette="tab10")
        plt.title("Relationship Between HDI and GDP per Capita by Region")
        plt.xlabel("GDP per capita (USD)")
        plt.ylabel("HDI")
        plt.legend(title="Region")
        plt.show()
    else:
        print("Columns 'GDP per capita (USD)' or 'HDI' are missing from the dataset.")

def export_cleaned_dataset():
    """Clean missing values and save the dataset."""
    numeric_data = data.select_dtypes(include=['number'])
    data_filled = data.copy()
    data_filled[numeric_data.columns] = numeric_data.fillna(numeric_data.mean())
    output_path = '../../Processed DataSet/Phase II/Modified_Dataset.csv'
    data_filled.to_csv(output_path, index=False)
    print(f"Cleaned dataset saved to: {output_path}")

# **Interactive Menu**
menu_options = {
    1: ("Display Summary Statistics", display_statistics),
    2: ("Plot Missing Values", plot_missing_values),
    3: ("Plot Correlation Matrix", plot_correlation),
    4: ("Plot Pairwise Relationships", plot_pairwise_relationships),
    5: ("Plot Distributions", plot_distributions),
    6: ("Analyze HDI and GDP Relationships", plot_relationships),
    7: ("Export Cleaned Dataset", export_cleaned_dataset),
    0: ("Exit", exit)
}

def display_menu():
    """Display the interactive menu."""
    while True:
        print("\n--- Dataset Analysis Menu ---")
        for key, (desc, _) in menu_options.items():
            print(f"{key}. {desc}")
        
        try:
            choice = int(input("\nEnter your choice: "))
            if choice in menu_options:
                menu_options[choice][1]()  # Execute the corresponding function
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Run the interactive menu
display_menu()
