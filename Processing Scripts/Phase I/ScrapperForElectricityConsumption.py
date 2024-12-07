import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_electricity_consumption'

# Send a GET request to the URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the first table with the 'wikitable' class
table = soup.find('table', {'class': 'wikitable'})

# Extract table headers
headers = [header.text.strip() for header in table.find_all('th')]

# Extract table rows with column alignment check
rows = []
for row in table.find_all('tr')[1:]:  # Skip the header row
    cells = row.find_all(['td', 'th'])
    row_data = [cell.text.strip() for cell in cells]
    
    # Adjust row length to match headers length by filling missing values, if any
    if len(row_data) < len(headers):
        row_data.extend([''] * (len(headers) - len(row_data)))  # Fill with empty strings
    elif len(row_data) > len(headers):
        row_data = row_data[:len(headers)]  # Trim extra columns if any

    rows.append(row_data)

# Create a DataFrame
df = pd.DataFrame(rows, columns=headers)

# Sort by "Location" column alphabetically, if it exists
if 'Location' in df.columns:
    df = df.sort_values(by='Location')

# Save the sorted DataFrame to CSV
df.to_csv('Electricity_Consumption_First_Table.csv', index=False)

print("Table has been successfully saved to 'Electricity_Consumption_First_Table.csv'.")
