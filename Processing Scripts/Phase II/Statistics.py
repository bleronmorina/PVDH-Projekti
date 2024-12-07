import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# **Ngarkimi i Dataset-it**
file_path = '../../Processed DataSet/Phase I/Merged_HDI_WorldBank_Data v3.csv'

try:
    data = pd.read_csv(file_path)
    print("Dataset-i u ngarkua me sukses.")
except FileNotFoundError:
    print(f"Gabim: Dataset-i nuk u gjet në {file_path}. Ju lutem kontrolloni rrugën e skedarit.")
    exit()

# **1. Statistika Përmbledhëse**
print("\nStatistika Përmbledhëse të Kolonave Numerike:")
print(data.describe())

# **2. Kontrolli i Vlerave të Munguar**
missing_values = data.isnull().sum()
print("\nVlerat e Munguar për Çdo Kolonë:")
print(missing_values[missing_values > 0])  # Shfaq vetëm kolonat me mungesa

# Vizualizimi i vlerave të munguar
plt.figure(figsize=(10, 6))
sns.heatmap(data.isnull(), cbar=False, cmap="viridis")
plt.title("Vlerat e Munguar në Dataset")
plt.show()

# **3. Korelacioni Multivariat (Vetëm Kolonat Numerike)**
numeric_data = data.select_dtypes(include=['number'])
correlation_matrix = numeric_data.corr()

print("\nMatrica e Korelacionit (Kolonat Numerike):")
print(correlation_matrix)

# Vizualizimi i Matricës së Korelacionit
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title("Matrica e Korelacionit")
plt.show()

# **4. Analizë Grafike - Grafet e Shpërndarjes**
# Zgjedhja e kolonave kryesore për analizë
columns_to_plot = ['HDI', 'GDP per capita (USD)', 'Life expectancy at birth (years)', 
                   'Individuals using the Internet (%)']
for column in columns_to_plot:
    if column in data.columns:
        sns.histplot(data[column].dropna(), kde=True, bins=30)
        plt.title(f"Shpërndarja e {column}")
        plt.xlabel(column)
        plt.ylabel("Frekuenca")
        plt.show()

# **5. Trajtimi i Vlerave të Munguar**
# Zëvendësimi i vlerave të munguar me mesataren për kolonat numerike
data_filled = data.copy()
data_filled[numeric_data.columns] = numeric_data.fillna(numeric_data.mean())
print("\nKontrolli i Dataset-it pas zëvendësimit të vlerave të munguar:")
print(data_filled.isnull().sum().sum(), "vlera të munguar në total.")

# **6. Analiza e Lidhjes Midis HDI dhe GDP per Capita**
if 'GDP per capita (USD)' in data.columns and 'HDI' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='GDP per capita (USD)', y='HDI', hue='Region', palette="tab10")
    plt.title("Lidhja Midis HDI dhe GDP per Capita sipas Rajoneve")
    plt.xlabel("GDP per capita (USD)")
    plt.ylabel("HDI")
    plt.legend(title="Rajoni")
    plt.show()
else:
    print("\nKolonat 'GDP per capita (USD)' ose 'HDI' mungojnë në dataset.")

# **7. Ruajtja e Dataset-it të Modifikuar**
output_path = '../../Processed DataSet/Phase II/Modified_Dataset.csv'
data_filled.to_csv(output_path, index=False)
print(f"Dataset-i i modifikuar u ruajt në: {output_path}")
