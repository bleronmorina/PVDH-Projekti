# PVDH-Projekti

Projekti nga lënda "Përgatitja dhe vizualizimi i të dhënave"

### Detyrat për Pjesën e I-rë - (15%)

- **Para-procesimi për Përgatitjen e të Dhënave për Analizë**

  - Mbledhja e të dhënave, definimi i tipeve të dhënave, dhe vlerësimi i kualitetit të të dhënave.
  - Integrimi, agregimi, mostrimi, dhe pastrimi i të dhënave.
  - Identifikimi dhe strategjia e trajtimit për vlerat e zbrazëta.

- **Reduktimi i Dimensionit dhe Përpunimi i Vetive**
  - Zgjedhja e nën-bashkësisë së vetive dhe krijimi i vetive të reja.
  - Diskretizimi, binarizimi, dhe transformimi i të dhënave.

## Data Collection

For the collection of data for the World Economic Indicators dataset, various reliable sources were used, including data from the World Bank and the Human Development Index (HDI) from the United Nations (UN). The World Bank data covers the period from 1960 to 2018 and includes various economic and development indicators, such as electricity consumption, GDP per capita, life expectancy, and many others.

To add more information on the social and economic development of countries, data from the HDI was included, which encompasses additional indicators related to life expectancy, GDP per capita, and educational achievements for each country from 1990 to 2021. This data was used to track development, environmental impact, and inequality across different countries.

Since the data is divided into 3 tables with a total of 12,657 records and 58 fields, it is important to structure and prepare it in a way that facilitates analysis. The data includes temporal and spatial variables, which help track changes over the years in different countries.

This data collection process aims to provide a comprehensive view of economic and social indicators for global development, enabling analysis of economic growth, improvements in healthcare and education, as well as differences between high- and low-income countries.

## Defining Data Types

| Table     | Field                                                        | Data Type | Description                                                                                  |
| --------- | ------------------------------------------------------------ | --------- | -------------------------------------------------------------------------------------------- |
| WorldBank | Country Name                                                 | String    | The name of the country                                                                      |
| WorldBank | Country Code                                                 | String    | The three-letter code representing the country                                               |
| WorldBank | Region                                                       | String    | The World Bank region of the country                                                         |
| WorldBank | IncomeGroup                                                  | String    | The World Bank Income Group of the country                                                   |
| WorldBank | Year                                                         | Integer   | The Year in which the statistics were recorded                                               |
| WorldBank | Birth rate, crude (per 1,000 people)                         | Float     | The Birth rate per 1000 people in the country                                                |
| WorldBank | Death rate, crude (per 1,000 people)                         | Float     | The death rate per 1000 people in the country                                                |
| WorldBank | Electric power consumption (kWh per capita)                  | Float     | The electricity consumption per person in kilowatt-hours in the country                      |
| WorldBank | GDP (USD)                                                    | Float     | The gross domestic product, or total economic output of the country                          |
| WorldBank | GDP per capita (USD)                                         | Float     | The gross domestic product, or economic output per person in the country                     |
| WorldBank | Individuals using the Internet (% of population)             | Float     | The percentage of individuals using the internet in each country                             |
| WorldBank | Infant mortality rate (per 1,000 live births)                | Float     | The infant mortality rate per 1000 births in the country                                     |
| WorldBank | Life expectancy at birth (years)                             | Float     | The life expectancy in years at birth in the country                                         |
| WorldBank | Population density (people per sq. km of land area)          | Float     | The number of people per square kilometer in the country                                     |
| WorldBank | Unemployment (% of total labor force) (modeled ILO estimate) | Float     | The percentage of the labor force that is not employed                                       |
| hdi       | iso3                                                         | String    | The three-letter code representing the country                                               |
| hdi       | country                                                      | String    | The name of the country                                                                      |
| hdi       | hdicode                                                      | String    | The HDI grouping from the UN                                                                 |
| hdi       | region                                                       | String    | The UNDP development regions                                                                 |
| hdi       | hdi_rank_2021                                                | Integer   | The country's HDI rank in 2021                                                               |
| hdi       | hdi_xxxx                                                     | Float     | The country's HDI in year xxxx                                                               |
| hdi       | le_xxxx                                                      | Float     | The country's life expectancy in year xxxx                                                   |
| hdi       | eys_xxxx                                                     | Float     | The country's expected years of schooling                                                    |
| hdi       | mys_xxxx                                                     | Float     | The country's mean years of schooling                                                        |
| hdi       | gnipc_xxxx                                                   | Float     | The gross national income per capita in 2017 PPP dollars                                     |
| hdi       | gdi_group_2021                                               | String    | The Gender Development Group                                                                 |
| hdi       | gdi_xxxx                                                     | Float     | Gender Development Index in year xxxx                                                        |
| hdi       | hdi_f_xxxx                                                   | Float     | Female HDI in year xxxx                                                                      |
| hdi       | le_f_xxxx                                                    | Float     | Female life expectancy at birth in year xxxx                                                 |
| hdi       | eys_f_xxxx                                                   | Float     | Female expected years of schooling in year xxxx                                              |
| hdi       | mys_f_xxxx                                                   | Float     | Female mean years of schooling in year xxxx                                                  |
| hdi       | gni_pc_f_xxxx                                                | Float     | Female GNI per capita in year xxxx                                                           |
| hdi       | hdi_m_xxxx                                                   | Float     | Male HDI in year xxxx                                                                        |
| hdi       | le_m_xxxx                                                    | Float     | Male life expectancy at birth in year xxxx                                                   |
| hdi       | eys_m_xxxx                                                   | Float     | Male expected years of schooling in year xxxx                                                |
| hdi       | mys_m_xxxx                                                   | Float     | Male mean years of schooling in year xxxx                                                    |
| hdi       | gni_pc_m_xxxx                                                | Float     | Male GNI per capita in year xxxx                                                             |
| hdi       | ihdi_xxxx                                                    | Float     | Inequality Adjusted HDI in year xxxx                                                         |
| hdi       | coef_ineq_xxxx                                               | Float     | Coefficient of human inequality in year xxxx                                                 |
| hdi       | loss_xxxx                                                    | Float     | Overall loss (%) in year xxxx                                                                |
| hdi       | ineq_le_xxxx                                                 | Float     | Inequality in life expectancy in year xxxx                                                   |
| hdi       | ineq_edu_xxxx                                                | Float     | Inequality in education in year xxxx                                                         |
| hdi       | ineq_inc_xxxx                                                | Float     | Inequality in income in year xxxx                                                            |
| hdi       | gii_rank_2021                                                | Integer   | Gender Inequality index rank in 2021                                                         |
| hdi       | gii_xxxx                                                     | Float     | Gender inequality index in year xxxx                                                         |
| hdi       | mmr_xxxx                                                     | Float     | Maternal Mortality Ratio (deaths per 100,000 live births) in year xxxx                       |
| hdi       | abr_xxxx                                                     | Float     | Adolescent birth rate (births per 1000 women aged 15-19) in year xxxx                        |
| hdi       | se_f_xxxx                                                    | Float     | Population with at least some secondary education, female (% ages 25 and older) in year xxxx |
| hdi       | se_m_xxxx                                                    | Float     | Population with at least some secondary education, male (% ages 25 and older) in year xxxx   |
| hdi       | pr_f_xxxx                                                    | Float     | Share of seats in parliament, female (% held by women) in year xxxx                          |
| hdi       | pr_m_xxxx                                                    | Float     | Share of seats in parliament, male (% held by men) in year xxxx                              |
| hdi       | lfpr_f_xxxx                                                  | Float     | Labour force participation rate, female (% ages 15 and older) in year xxxx                   |
| hdi       | lfpr_m_xxxx                                                  | Float     | Labour force participation rate, male (% ages 15 and older) in year xxxx                     |
| hdi       | rankdiff_hdi_phdi_2021                                       | Integer   | Difference in HDI rank from 2020                                                             |
| hdi       | phdi_xxxx                                                    | Float     | Planetary pressures-adjusted Human Development Index (value) in year xxxx                    |
| hdi       | diff_hdi_phdi_xxxx                                           | Float     | Difference from HDI value (%) in year xxxx                                                   |
| hdi       | co2_prod_xxxx                                                | Float     | Carbon dioxide emissions per capita (production) (tonnes) in year xxxx                       |
| hdi       | mf_xxxx                                                      | Float     | Material footprint per capita (tonnes) in year xxxx                                          |

## Preprocessing Data

## Data Transformation: Reshaping and Reducing Columns

### Overview

The original dataset contained many columns, with each indicator represented separately for each year (e.g., `GDP_1990`, `GDP_1991`). To improve usability, the dataset was transformed from a "wide" format to a "long" format, where each indicator-year pair became a separate row. This approach allows for more flexible analysis of indicators over time.

### Transformation Process

The following steps describe the transformation process:

1. **Melting the Data**:

   - The dataset was reshaped using a "melt" function, which converted each year-specific indicator column into a separate row.
   - This reduced the width of the dataset and allowed us to treat each year of an indicator as an individual observation.

2. **Extracting Indicator and Year**:

   - We extracted two distinct columns from the combined `indicator_year` column:
     - `indicator`: representing the name of each indicator (e.g., `GDP`, `Life_Expectancy`).
     - `year`: representing the specific year of the indicator.
   - This involved splitting strings in `indicator_year` (e.g., `GDP_1990`) into separate `indicator` and `year` columns for easier sorting and analysis.

3. **Pivoting to Reshape the Data**:
   - The data was reshaped again using a pivot table, converting the unique indicators back into columns with `year` as a separate variable.
   - This created a tidy structure where each row represents a unique combination of country, year, and a set of indicators.

### Column Removal: Simplifying the Dataset

As part of data preprocessing, several columns were removed from the dataset. This step was taken to focus on relevant indicators and reduce noise, ultimately streamlining the dataset for analysis. Below is a detailed explanation of each column removed and the rationale behind its exclusion.

#### Columns Removed

The following columns were removed from the dataset:

- `loss`
- `hdi_rank`
- `gii_rank`
- `gdi`
- `gdi_group`
- `rankdiff_hdi_phdi`

#### Reasons for Removal

Each column was evaluated for relevance to the project goals. Here’s why each of these columns was removed:

| Column Name         | Description                                                             | Reason for Removal                                                                                            |
| ------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `loss`              | Indicates a percentage loss in human development due to inequality.     | The dataset already includes other inequality metrics, making this metric redundant for our analysis.         |
| `hdi_rank`          | Global rank of each country based on the Human Development Index (HDI). | Rankings are less informative than HDI scores themselves and can be biased by annual changes or fluctuations. |
| `gii_rank`          | Global rank of each country based on the Gender Inequality Index (GII). | Similar to `hdi_rank`, this rank offers limited analytical value compared to the GII score itself.            |
| `gdi`               | Gender Development Index, comparing HDI values between men and women.   | This was removed to avoid duplication, as other gender-disaggregated metrics are included separately.         |
| `gdi_group`         | Classification based on the Gender Development Index.                   | Categorical grouping based on `gdi`, which isn’t needed for numerical analysis in this context.               |
| `rankdiff_hdi_phdi` | Difference in rank between HDI and inequality-adjusted HDI (pHDI).      | Analysis focuses on the HDI and pHDI values themselves; rank differences do not provide additional insight.   |

#### Summary

By removing these columns, the dataset now focuses on core indicators that directly contribute to the analysis. This step reduces complexity and ensures that only the most relevant data points are retained, improving both the efficiency and clarity of further data processing and modeling.

### Scripts and Processed Datasets

- **MergeCode.py**  
  A processing script that combines unprocessed datasets into a single dataset based on the `CountryCode` and `Year` columns. This script also filters for `Year >= 1990`, as most rows before 1990 contain limited data.

- **MergeCode v2.py**  
  An updated processing script that merges the processed datasets into a single dataset. This version also incorporates data from a new file, `Countries.csv`, to enhance country-specific information.

- **CountryNormalization.py**  
  A processing script that extracts all unique country information from the World Bank CSV file, creating a new file called `Countries.csv` with these unique values. It then fetches data from the HDI and World Bank datasets, removing extra country columns to standardize them. When additional country information is needed, this dataset or a join operation with `Countries.csv` can be used.

### Processed Datasets

- **Merged_HDI_WorldBank_Data.csv**  
  A processed dataset created by merging the unprocessed HDI and World Bank datasets, using `CountryCode` and `Year` as the keys.

- **Merged_HDI_WorldBank_Data v2.csv**  
  A refined processed dataset similar to the previous version but using the processed datasets `HDI Data v3`, `WorldBank v2`, and `Countries.csv` as merge sources.

- **HDI Data v3.csv**  
  A processed dataset without the extra columns `country` and `region`.

- **WorldBank v2.csv**  
  A processed dataset without the extra columns `Country Name` and `Region`.

## Defining Data Types After Table Integration

| Table                                     | Field                                                        | Data Type | Description                                                                                  |
| ----------------------------------------- | ------------------------------------------------------------ | --------- | -------------------------------------------------------------------------------------------- |
| Merged \_HDI_Worldbank_Data v2, Countries | Country Code                                                 | String    | The three letter code representing the country                                               |
| Countries                                 | Country                                                      | String    | The name of the country                                                                      |
| Countries                                 | Region                                                       | String    | The World Bank region of the country                                                         |
| Merged \_HDI_Worldbank_Data v2            | hdicode                                                      | String    | The HDI grouping from the UN                                                                 |
| Merged \_HDI_Worldbank_Data v2            | Year                                                         | Integer   | The Year in which the statistics were recorded                                               |
| Merged \_HDI_Worldbank_Data v2            | co2_prod                                                     | Float     | Carbon dioxide emissions per capita (production) (tonnes)                                    |
| Merged \_HDI_Worldbank_Data v2            | abr                                                          | Float     | Adolescent birth rate (births per 1000 women aged 15-19)                                     |
| Merged \_HDI_Worldbank_Data v2            | coef_ineq                                                    | Float     | Coefficient of human inequality                                                              |
| Merged \_HDI_Worldbank_Data v2            | diff_hdi_phdi                                                | Float     | Difference from HDI value (%)                                                                |
| Merged \_HDI_Worldbank_Data v2            | eys                                                          | Float     | The country's expected years of schooling                                                    |
| Merged \_HDI_Worldbank_Data v2            | eys_f                                                        | Float     | Female expected years of schooling                                                           |
| Merged \_HDI_Worldbank_Data v2            | eys_m                                                        | Float     | Male expected years of schooling                                                             |
| Merged \_HDI_Worldbank_Data v2            | gii                                                          | Float     | Gender inequality index                                                                      |
| Merged \_HDI_Worldbank_Data v2            | gni_pc_f                                                     | Float     | Female GNI per capita                                                                        |
| Merged \_HDI_Worldbank_Data v2            | gni_pc_m                                                     | Float     | Male GNI per capita                                                                          |
| Merged \_HDI_Worldbank_Data v2            | gnipc                                                        | Float     | The gross national income per capita in 2017 PPP dollars                                     |
| Merged \_HDI_Worldbank_Data v2            | hdi                                                          | Float     | The country's HDI                                                                            |
| Merged \_HDI_Worldbank_Data v2            | hdi_f                                                        | Float     | Female HDI                                                                                   |
| Merged \_HDI_Worldbank_Data v2            | hdi_m                                                        | Float     | Male HDI                                                                                     |
| Merged \_HDI_Worldbank_Data v2            | ihdi                                                         | Float     | Inequality Adjusted HDI                                                                      |
| Merged \_HDI_Worldbank_Data v2            | ineq_edu                                                     | Float     | Inequality in education                                                                      |
| Merged \_HDI_Worldbank_Data v2            | ineq_inc                                                     | Float     | Inequality in income                                                                         |
| Merged \_HDI_Worldbank_Data v2            | ineq_le                                                      | Float     | Inequality in life expectancy                                                                |
| Merged \_HDI_Worldbank_Data v2            | le                                                           | Float     | The country's life expectancy                                                                |
| Merged \_HDI_Worldbank_Data v2            | le_f                                                         | Float     | Female life expectancy at birth                                                              |
| Merged \_HDI_Worldbank_Data v2            | le_m                                                         | Float     | Male life expectancy at birth                                                                |
| Merged \_HDI_Worldbank_Data v2            | lfpr_f                                                       | Float     | Labour force participation rate, female (% ages 15 and older)                                |
| Merged \_HDI_Worldbank_Data v2            | lfpr_m                                                       | Float     | Labour force participation rate, male (% ages 15 and older)                                  |
| Merged \_HDI_Worldbank_Data v2            | mf                                                           | Float     | Material footprint per capita (tonnes)                                                       |
| Merged \_HDI_Worldbank_Data v2            | mmr                                                          | Float     | Maternal Mortality Ratio (deaths per 100,000 live births)                                    |
| Merged \_HDI_Worldbank_Data v2            | mys                                                          | Float     | The country's mean years of schooling                                                        |
| Merged \_HDI_Worldbank_Data v2            | mys_f                                                        | Float     | Female mean years of schooling                                                               |
| Merged \_HDI_Worldbank_Data v2            | mys_m                                                        | Float     | Male mean years of schooling                                                                 |
| Merged \_HDI_Worldbank_Data v2            | phdi                                                         | Float     | Planetary pressures-adjusted Human Development Index (value)                                 |
| Merged \_HDI_Worldbank_Data v2            | pr_f                                                         | Float     | Share of seats in parliament, female (% held by women)                                       |
| Merged \_HDI_Worldbank_Data v2            | pr_m                                                         | Float     | Share of seats in parliament, male (% held by men)                                           |
| Merged \_HDI_Worldbank_Data v2            | se_f                                                         | Float     | Population with at least some secondary education, female (% ages 25 and older) in year xxxx |
| Merged \_HDI_Worldbank_Data v2            | se_m                                                         | Float     | Population with at least some secondary education, male (% ages 25 and older) in year xxxx   |
| Merged \_HDI_Worldbank_Data v2            | IncomeGroup                                                  | String    | The World Bank Income Group of the country                                                   |
| Merged \_HDI_Worldbank_Data v2            | Birth rate, crude (per 1,000 people)                         | Float     | The Birth rate per 1000 people in the country                                                |
| Merged \_HDI_Worldbank_Data v2            | Death rate, crude (per 1,000 people)                         | Float     | The death rate per 1000 people in the country                                                |
| Merged \_HDI_Worldbank_Data v2            | Electric power consumption (kWh per capita)                  | Float     | The electricity consumption per person in kilowatt-hours in the country                      |
| Merged \_HDI_Worldbank_Data v2            | GDP (USD)                                                    | Float     | The gross domestic product, or total economic output of the country                          |
| Merged \_HDI_Worldbank_Data v2            | GDP per capita (USD)                                         | Float     | The gross domestic product, or economic output per person in the country                     |
| Merged \_HDI_Worldbank_Data v2            | Individuals using the Internet (% of population)             | Float     | The percentage of individuals using the internet in each country                             |
| Merged \_HDI_Worldbank_Data v2            | Infant mortality rate (per 1,000 live births)                | Float     | The infant mortality rate per 1000 births in the country                                     |
| Merged \_HDI_Worldbank_Data v2            | Life expectancy at birth (years)                             | Float     | The life expectancy in years at birth in the country                                         |
| Merged \_HDI_Worldbank_Data v2            | Population density (people per sq. km of land area)          | Float     | The number of people per square kilometer in the country                                     |
| Merged \_HDI_Worldbank_Data v2            | Unemployment (% of total labor force) (modeled ILO estimate) | Float     | The percentage of the labor force that is not employed                                       |

### Missing Data Percentage per Column

| Column                                                         | Missing Data (%) |
| -------------------------------------------------------------- | ---------------- |
| `co2_prod`                                                     | 0.50             |
| `coef_ineq`                                                    | 78.25            |
| `diff_hdi_phdi`                                                | 27.47            |
| `eys`                                                          | 4.11             |
| `eys_f`                                                        | 11.36            |
| `eys_m`                                                        | 11.36            |
| `gii`                                                          | 23.78            |
| `gni_pc_f`                                                     | 7.18             |
| `gni_pc_m`                                                     | 7.18             |
| `gnipc`                                                        | 1.02             |
| `hdi`                                                          | 11.17            |
| `hdi_f`                                                        | 23.83            |
| `hdi_m`                                                        | 23.83            |
| `ihdi`                                                         | 78.25            |
| `ineq_edu`                                                     | 74.28            |
| `ineq_inc`                                                     | 77.07            |
| `ineq_le`                                                      | 68.97            |
| `lfpr_f`                                                       | 6.16             |
| `lfpr_m`                                                       | 6.16             |
| `mf`                                                           | 22.15            |
| `mmr`                                                          | 3.42             |
| `mys`                                                          | 9.52             |
| `mys_f`                                                        | 14.93            |
| `mys_m`                                                        | 14.93            |
| `phdi`                                                         | 27.47            |
| `pr_f`                                                         | 10.04            |
| `pr_m`                                                         | 10.04            |
| `se_f`                                                         | 15.30            |
| `se_m`                                                         | 15.28            |
| `Birth rate, crude (per 1,000 people)`                         | 5.64             |
| `Death rate, crude (per 1,000 people)`                         | 5.72             |
| `Electric power consumption (kWh per capita)`                  | 43.72            |
| `GDP (USD)`                                                    | 3.71             |
| `GDP per capita (USD)`                                         | 3.78             |
| `Individuals using the Internet (% of population)`             | 18.78            |
| `Life expectancy at birth (years)`                             | 6.66             |
| `Population density (people per sq. km of land area)`          | 1.65             |
| `Unemployment (% of total labor force) (modeled ILO estimate)` | 9.40             |
