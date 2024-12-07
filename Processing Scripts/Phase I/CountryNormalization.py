import pandas as pd

# Files qe i perdorim si input
WorldBankV1File = 'Processed DataSet/WorldBank v1.csv' 
HDIDataV2File = 'Processed DataSet/HDI Data v2.csv' 

# Files te reja qe i perdorim si output
CountriesFile = 'Processed DataSet/Countries.csv'
WorldBankV2File = 'Processed DataSet/WorldBank v2.csv' 
HDIDataV3File = 'Processed DataSet/HDI Data v3.csv' 


# Hapi 1: Krijojme tabelen Countries, sipas shteteve unike ne WorldBank csv
columns_to_load = ['Country Code', 'Country Name', 'Region']
source_df = pd.read_csv(WorldBankV1File, usecols=columns_to_load)

unique_countries_df = source_df.drop_duplicates(subset='Country Code')

final_countries_df = pd.DataFrame({
    'CountryCode': unique_countries_df['Country Code'],
    'Country': unique_countries_df['Country Name'],
    'Region': unique_countries_df['Region']
})

# Keto jane rreshta shtese ne tabelen HDI Data, qe nuk reprezentojne shtete, por grupim te shteteve
custom_rows = [
    {'CountryCode': 'ZZA.VHHD', 'Country': 'Very high human development', 'Region': ''},
    {'CountryCode': 'ZZB.HHD', 'Country': 'High human development', 'Region': ''},
    {'CountryCode': 'ZZC.MHD', 'Country': 'Medium human development', 'Region': ''},
    {'CountryCode': 'ZZD.LHD', 'Country': 'Low human development', 'Region': ''},
    {'CountryCode': 'ZZE.AS', 'Country': 'Arab States', 'Region': ''},
    {'CountryCode': 'ZZF.EAP', 'Country': 'East Asia and the Pacific', 'Region': ''},
    {'CountryCode': 'ZZG.ECA', 'Country': 'Europe and Central Asia', 'Region': ''},
    {'CountryCode': 'ZZH.LAC', 'Country': 'Latin America and the Caribbean', 'Region': ''},
    {'CountryCode': 'ZZI.SA', 'Country': 'South Asia', 'Region': ''},
    {'CountryCode': 'ZZJ.SSA', 'Country': 'Sub-Saharan Africa', 'Region': ''},
    {'CountryCode': 'ZZK.WORLD', 'Country': 'World', 'Region': ''}
]

custom_rows_df = pd.DataFrame(custom_rows)

final_countries_df = pd.concat([final_countries_df, custom_rows_df], ignore_index=True)

final_countries_df.to_csv(CountriesFile, index=False)


# Hapi 2: Krijojme verzionin e ri `WorldBank v2.csv`, eleminojme (pastrojme) kolonat shtese te Countries ne menyre qe ato pastaj ti lidhim ne Merge
world_bank_df = pd.read_csv(WorldBankV1File)
world_bank_df_cleaned = world_bank_df.drop(columns=['Country Name', 'Region'])
world_bank_df_cleaned.to_csv(WorldBankV2File, index=False)

# Hapi 3: Krijojme verzionin e ri `HDI Data v3.csv`, eleminojme (pastrojme) kolonat shtese te Countries ne menyre qe ato pastaj ti lidhim ne Merge

hdi_df = pd.read_csv(HDIDataV2File)
hdi_df_cleaned = hdi_df.drop(columns=['country', 'region'])
hdi_df_cleaned.to_csv(HDIDataV3File, index=False)