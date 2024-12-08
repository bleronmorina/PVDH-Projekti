
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# **File Paths**
file_path_initial = '../../Processed DataSet/Phase I/Merged_HDI_WorldBank_Data v3.csv'
file_path_cleaned = '../../Processed DataSet/Phase II/Removed_Fake_Discoveries.csv'

# **Load Datasets**
try:
    data_initial = pd.read_csv(file_path_initial)
    data_cleaned = pd.read_csv(file_path_cleaned)
    print("Datasets loaded successfully.")
except FileNotFoundError as e:
    print(f"Error: {e}")
    exit()

# Set default dataset for analysis
data = data_cleaned

# **Helper Functions**

def display_statistics(dataset):
    """Show key statistics for a dataset."""
    print("\nSummary Statistics (Numerical Columns):")
    print(dataset.describe())
    print("\nSummary Statistics (Categorical Columns):")
    print(dataset.describe(include=['object']))
    print("\nMissing Values in Each Column:")
    missing_values = dataset.isnull().sum()
    print(missing_values[missing_values > 0])

def plot_missing_values(dataset):
    """Visualize missing values in a dataset."""
    plt.figure(figsize=(10, 6))
    sns.heatmap(dataset.isnull(), cbar=False, cmap="viridis")
    plt.title("Missing Values in the Dataset")
    plt.show()

def compare_missing_values():
    """Compare missing values between initial and cleaned datasets."""
    initial_missing = data_initial.isnull().sum()
    cleaned_missing = data_cleaned.isnull().sum()
    
    comparison = pd.DataFrame({
        "Initial Missing": initial_missing,
        "Cleaned Missing": cleaned_missing
    }).query("`Initial Missing` > 0 or `Cleaned Missing` > 0")
    
    print("\nComparison of Missing Values:")
    print(comparison)

def plot_correlation(dataset):
    """Plot the correlation matrix for numerical data in a dataset."""
    numeric_data = dataset.select_dtypes(include=['number'])
    correlation_matrix = numeric_data.corr()

    # Display correlation matrix
    print("\nCorrelation Matrix (Top 5 Relationships):")
    print(correlation_matrix.unstack().sort_values(key=lambda x: abs(x), ascending=False)[1:6])

    # Visualize the correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=False, cmap="coolwarm", cbar=True, square=True)
    plt.title("Correlation Matrix (Simplified)")
    plt.show()

def plot_pairwise_relationships(dataset):
    """Plot pairwise relationships for key columns in a dataset."""
    columns_to_plot = ['HDI', 'GDP per capita (USD)', 'Life expectancy at birth (years)', 
                       'Individuals using the Internet (%)']
    available_columns = [col for col in columns_to_plot if col in dataset.columns]
    
    if available_columns:
        sns.pairplot(dataset[available_columns])
        plt.suptitle("Pairwise Relationships for Key Variables", y=1.02)
        plt.show()
    else:
        print("Key columns for pairwise relationships are not present in the dataset.")

def plot_distributions(dataset):
    """Plot distributions of key numerical and categorical columns in a dataset."""
    # Numerical column distributions
    columns_to_plot = ['HDI', 'GDP per capita (USD)', 'Life expectancy at birth (years)', 
                       'Individuals using the Internet (%)']
    for column in columns_to_plot:
        if column in dataset.columns:
            sns.histplot(dataset[column].dropna(), kde=True, bins=30, color='blue')
            plt.title(f"Distribution of {column}")
            plt.xlabel(column)
            plt.ylabel("Frequency")
            plt.show()

    # Categorical column distributions (excluding 'Country' and 'Country Code')
    excluded_columns = ['Country', 'Country Code']
    categorical_cols = [
        column for column in dataset.select_dtypes(include=['object']).columns
        if column not in excluded_columns
    ]
    for column in categorical_cols:
        sns.countplot(y=dataset[column], order=dataset[column].value_counts().index)
        plt.title(f"Category Distribution for {column}")
        plt.show()

def plot_relationships(dataset):
    """Analyze relationships between HDI and GDP per capita in a dataset."""
    if 'GDP per capita (USD)' in dataset.columns and 'hdi' in dataset.columns:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=dataset, x='GDP per capita (USD)', y='hdi', hue='Region', palette="tab10")
        plt.title("Relationship Between HDI and GDP per Capita by Region")
        plt.xlabel("GDP per capita (USD)")
        plt.ylabel("HDI")
        plt.legend(title="Region")
        plt.show()
    else:
        print("Columns 'GDP per capita (USD)' or 'hdi' are missing from the dataset.")


def plot_time_trends(dataset):
    """Plot trends over time for key variables."""
    if 'Year' in dataset.columns:
        time_columns = ['HDI', 'GDP per capita (USD)', 'Life expectancy at birth (years)']
        for column in time_columns:
            if column in dataset.columns:
                sns.lineplot(data=dataset, x='Year', y=column, hue='Region', marker='o')
                plt.title(f"Trend of {column} Over Time")
                plt.xlabel("Year")
                plt.ylabel(column)
                plt.legend(title="Region", loc='best')
                plt.show()
    else:
        print("No 'Year' column found in the dataset.")

# **Interactive Menu**
menu_options = {
    1: ("Display Summary Statistics (Current Dataset)", lambda: display_statistics(data)),
    2: ("Plot Missing Values (Current Dataset)", lambda: plot_missing_values(data)),
    3: ("Compare Missing Values (Initial vs Cleaned)", compare_missing_values),
    4: ("Plot Correlation Matrix (Current Dataset)", lambda: plot_correlation(data)),
    5: ("Plot Pairwise Relationships (Current Dataset)", lambda: plot_pairwise_relationships(data)),
    6: ("Plot Distributions (Current Dataset)", lambda: plot_distributions(data)),
    7: ("Analyze HDI and GDP Relationships (Current Dataset)", lambda: plot_relationships(data)),
    8: ("Plot Time Trends (Current Dataset)", lambda: plot_time_trends(data)),
    9: ("Switch to Initial Dataset", lambda: switch_dataset('initial')),
    10: ("Switch to Cleaned Dataset", lambda: switch_dataset('cleaned')),
    0: ("Exit", exit)
}

def switch_dataset(choice):
    """Switch between initial and cleaned datasets."""
    global data
    if choice == 'initial':
        data = data_initial
        print("Switched to Initial Dataset.")
    elif choice == 'cleaned':
        data = data_cleaned
        print("Switched to Cleaned Dataset.")
    else:
        print("Invalid dataset choice.")

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
