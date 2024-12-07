# PVDH-Projekti

Projekti nga lënda "Përgatitja dhe vizualizimi i të dhënave"

## Introductory Information

<img src="https://github.com/user-attachments/assets/9002855f-3f97-4b41-a180-85d1e24ad34a" alt="University Logo" width="150" align="right"/>

**University of Prishtina**  
**Faculty of Computer and Software Engineering**  
Master’s Program in **Computer and Software Engineering**  
Course: **Data preparation and visualization**

## Course Professor

- **Mergim Hoti**

## Project Team Members (Group 5)

- **Argjend Zekaj**
- **Bleron Morina**
- **Endrit Gjoka**

---

---

### Detyrat për Pjesën e I-rë - (15%)

- **Para-procesimi për Përgatitjen e të Dhënave për Analizë**

  - Mbledhja e të dhënave, definimi i tipeve të dhënave, dhe vlerësimi i kualitetit të të dhënave.
  - Integrimi, agregimi, mostrimi, dhe pastrimi i të dhënave.
  - Identifikimi dhe strategjia e trajtimit për vlerat e zbrazëta.

- **Reduktimi i Dimensionit dhe Përpunimi i Vetive**
  - Zgjedhja e nën-bashkësisë së vetive dhe krijimi i vetive të reja.
  - Diskretizimi, binarizimi, dhe transformimi i të dhënave.

---

## Data Collection

For the collection of data for the World Economic Indicators dataset, various reliable sources were used, including data from the World Bank and the Human Development Index (HDI) from the United Nations (UN). The World Bank data covers the period from 1960 to 2018 and includes various economic and development indicators, such as electricity consumption, GDP per capita, life expectancy, and many others.

To add more information on the social and economic development of countries, data from the HDI was included, which encompasses additional indicators related to life expectancy, GDP per capita, and educational achievements for each country from 1990 to 2021. This data was used to track development, environmental impact, and inequality across different countries.

Since the data is divided into 3 tables with a total of 12,657 records and 58 fields, it is important to structure and prepare it in a way that facilitates analysis. The data includes temporal and spatial variables, which help track changes over the years in different countries.

This data collection process aims to provide a comprehensive view of economic and social indicators for global development, enabling analysis of economic growth, improvements in healthcare and education, as well as differences between high- and low-income countries.

---

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

---

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

---

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

---

### Scripts and Processed Datasets

- **MergeCode.py**  
  A processing script that combines unprocessed datasets into a single dataset based on the `CountryCode` and `Year` columns. This script also filters for `Year >= 1990`, as most rows before 1990 contain limited data.

- **MergeCode v2.py**  
  An updated processing script that merges the processed datasets into a single dataset. This version also incorporates data from a new file, `Countries.csv`, to enhance country-specific information.

- **CountryNormalization.py**  
  A processing script that extracts all unique country information from the World Bank CSV file, creating a new file called `Countries.csv` with these unique values. It then fetches data from the HDI and World Bank datasets, removing extra country columns to standardize them. When additional country information is needed, this dataset or a join operation with `Countries.csv` can be used.

---

### Processed Datasets

- **Merged_HDI_WorldBank_Data.csv**  
  A processed dataset created by merging the unprocessed HDI and World Bank datasets, using `CountryCode` and `Year` as the keys.

- **Merged_HDI_WorldBank_Data v2.csv**  
  A refined processed dataset similar to the previous version but using the processed datasets `HDI Data v3`, `WorldBank v2`, and `Countries.csv` as merge sources.

- **HDI Data v3.csv**  
  A processed dataset without the extra columns `country` and `region`.

- **WorldBank v2.csv**  
  A processed dataset without the extra columns `Country Name` and `Region`.

---

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

---

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

---

## Data Scraping

- `Script: ScrapperForElectricityConsumption.py`
- `Purpose: This script scrapes Wikipedia to obtain the latest electricity consumption data for countries worldwide. It focuses on gathering specific metrics like consumption per capita, year, and population.`
- `Output: The data collected is saved as ElectricityConsumption.csv for further processing.`

---

## Handling Missing Values

- `Script: HandlingElectricityConsumptionMissingValues.py`
- `Purpose: This script takes the scraped data (ElectricityConsumption.csv) and fills in missing values for the "Electric power consumption (kWh per capita)" field in the WorldBank v2.csv dataset. It aligns records by the "Country      Code" field to ensure accurate matching and integration of values.`
- `Output: The final dataset with filled missing values is saved as WorldBank v3.csv.`

In the process of preparing the dataset, we encountered missing values in certain columns. After evaluating the nature and distribution of these missing values, we chose to ignore most of them (except for the Electricity Consumption, mentioned above) for the following reasons:

1. **Data Completeness for Core Analysis**: The majority of essential indicators had sufficient data coverage across countries and years, ensuring that core analyses would remain unaffected by the missing values. Key economic, health, and education metrics provided a complete enough dataset for our primary objectives.

2. **Maintaining Dataset Integrity**: Filling missing values, especially for indicators with sparse data coverage, could introduce bias or distort historical trends. Rather than risking inaccurate interpolations, we opted to work with available data, especially for cases where historical data was patchy or discontinuous.

3. **Focus on Reliable Trends**: Many of the missing values occurred in indicators that were not consistently tracked or recorded across countries or years, particularly in older records. Ignoring these missing values allows us to focus on trends that have reliable historical continuity without adding potentially misleading estimates.

4. **Impact on Temporal Analysis**: Temporal trends are a core part of our analysis, and many methods of imputing missing values, such as forward filling or averaging, would not preserve the accuracy of year-on-year changes. To retain the integrity of these trends, we chose to ignore missing values rather than apply potentially inappropriate imputation techniques.

### Data Column Subsets

The dataset contains a variety of indicators related to economic, demographic, health, and educational metrics. For clarity, the columns are organized into the following subsets:

---

#### 1. Identification and Basic Information

- `Country Code`: ISO3 country code.
- `Country`: Full country name.
- `Region`: Geographical region of the country.
- `hdicode`: HDI classification code.
- `Year`: The year of the data record.
- `IncomeGroup`: Income classification (e.g., Low, Middle, High).

---

#### 2. Economic Indicators

- `co2_prod`: CO2 production.
- `gnipc`: Gross National Income per capita.
- `gni_pc_f`: GNI per capita for females.
- `gni_pc_m`: GNI per capita for males.
- `GDP (USD)`: Gross Domestic Product in USD.
- `GDP per capita (USD)`: GDP per capita in USD.
- `Electric power consumption (kWh per capita)`: Per capita electricity consumption.
- `Unemployment (% of total labor force) (modeled ILO estimate)`: Unemployment rate based on ILO model.

---

#### 3. Health Indicators

- `abr`: Adolescent birth rate.
- `mmr`: Maternal mortality ratio.
- `Infant mortality rate (per 1,000 live births)`: Infant mortality rate.
- `Life expectancy at birth (years)`: Life expectancy.
- `le`: General life expectancy.
- `le_f`: Life expectancy for females.
- `le_m`: Life expectancy for males.
- `ihdi`: Inequality-adjusted HDI.
- `coef_ineq`: Coefficient of inequality.
- `ineq_edu`: Inequality in education.
- `ineq_inc`: Inequality in income.
- `ineq_le`: Inequality in life expectancy.
- `Individuals using the Internet (% of population)`: Internet usage percentage.

---

#### 4. Education Indicators

- `eys`: Expected years of schooling.
- `eys_f`: Expected years of schooling for females.
- `eys_m`: Expected years of schooling for males.
- `mys`: Mean years of schooling.
- `mys_f`: Mean years of schooling for females.
- `mys_m`: Mean years of schooling for males.
- `se_f`: School enrollment rate for females.
- `se_m`: School enrollment rate for males.
- `pr_f`: Primary school completion rate for females.
- `pr_m`: Primary school completion rate for males.
- `gii`: Gender Inequality Index.
- `mf`: Male-to-female ratio.

---

#### 5. Demographic Indicators

- `Population density (people per sq. km of land area)`: Population density.
- `Birth rate, crude (per 1,000 people)`: Crude birth rate.
- `Death rate, crude (per 1,000 people)`: Crude death rate.
- `lfpr_f`: Labor force participation rate for females.
- `lfpr_m`: Labor force participation rate for males.

---

#### 6. Human Development Index (HDI) and Related Metrics

- `hdi`: Human Development Index.
- `hdi_f`: HDI for females.
- `hdi_m`: HDI for males.
- `diff_hdi_phdi`: Difference between HDI and pHDI.
- `phdi`: Poverty-adjusted HDI.

---

Each subset is organized to provide a clear view of indicators in categories such as economic, health, education, demographic, and human development. This structure supports targeted analyses in each domain.

### Discretization, Binarization, and Feature Creation

In this project, there was no need to apply discretization or binarization techniques, nor was there a need to create or calculate new columns. Here’s why:

- **Discretization and Binarization**:  
  Discretization (converting continuous variables into discrete categories) and binarization (transforming data into binary form) are often useful for categorical or classification-based analyses. However, in this dataset, most variables were already well-suited for analysis in their continuous form. Discretizing or binarizing these continuous indicators would result in a significant loss of information, reducing the granularity needed for effective analysis of trends over time.

- **Feature Creation**:  
  New feature creation, or generating additional columns, was unnecessary because the dataset already contained a comprehensive set of indicators that adequately represent the data's underlying dimensions. The dataset includes variables that cover economic, educational, health, and environmental aspects, providing a well-rounded basis for analysis without needing additional derived features.

Thus, by keeping the data in its original form, we preserve its detail and ensure the dataset remains interpretable and aligned with the project’s goals.

---

### Explanation for Not Performing Aggregation

In this project, certain aggregation methods were not applied due to the following reasons:

1. **Temporal Aggregation**:

   - We chose not to average data over time periods (e.g., decades) or use snapshots from specific years. Instead, the dataset maintains yearly data to preserve the granularity of changes over time. This allows for detailed analysis of year-over-year trends, which would be lost with temporal aggregation.
   - By keeping yearly records intact, we retain the ability to observe shorter-term fluctuations and trends, which can be valuable for identifying patterns that might be obscured in broader averages.

2. **Geographic Aggregation**:

   - Data was not aggregated by region or income group in order to preserve individual country-level data. Aggregating by region could obscure country-specific trends and disparities, especially since countries within the same region may have significant differences in economic, social, and health indicators.
   - This approach ensures that we can conduct detailed analyses at the country level, providing a clearer picture of each country’s unique trajectory rather than generalizing across regions.

3. **Indicator-Specific Aggregation**:
   - Weighted averages or medians were not calculated for specific indicators, as our focus was on maintaining raw data values for each indicator. This decision was made to avoid assumptions about the relative importance of indicators across different countries.
   - Retaining individual values without weighting allows for more flexibility in analysis, as we can apply various techniques as needed without having pre-aggregated values that might influence results.

By not performing these aggregation methods, we preserved the full detail of the dataset, enabling a more granular analysis of trends and patterns on a year-by-year and country-by-country basis.

---

---

### Detyrat për Pjesën e II-të - (15%)

- **Detektimi i përjashtuesve.**
- **Mënjanimi i zbulimeve jo të sakta**
- **Eksplorimi i te dhënave: statistika përmbledhëse, multivariante.**

## Outlier Detection

This Python script (`Outliers.py`) is designed to detect and analyze potential outliers in a dataset using multiple statistical and machine learning methods. By combining traditional techniques like Z-Score and Interquartile Range (IQR) with advanced approaches like Isolation Forest, it provides a comprehensive view of data anomalies.

### Features

1. **Outlier Detection Methods:**
   - **Z-Score Method:** Identifies outliers based on the standard deviation of data points.
   - **IQR Method:** Flags outliers that fall outside the interquartile range.
   - **Isolation Forest:** A machine learning-based method for detecting anomalies.

2. **Visualization:**
   - Generates boxplots for numerical columns to visualize potential outliers.

3. **Results:**
   - Saves detected outliers to a separate file (`Detected_Outliers.csv`).
   - Outputs a cleaned dataset without outliers (`Cleaned_Data.csv`).

4. **Summary Statistics:**
   - Provides a detailed count of outliers detected by each method and combined results.

### How It Works

1. **Load the Dataset:**
   The script reads the dataset (`Modifiet_Dataset.csv`) and focuses on numerical columns for outlier detection.

2. **Apply Outlier Detection Methods:**
   - **Z-Score:** Flags data points with a Z-score greater than 3.
   - **IQR:** Identifies outliers beyond 1.5 times the interquartile range.
   - **Isolation Forest:** Uses a contamination rate of 1% to detect anomalies.

3. **Combine Results:**
   Outliers detected by any method are flagged as combined outliers.

4. **Visualize and Save Results:**
   - Displays boxplots for better understanding.
   - Saves both outliers and a cleaned dataset for further analysis.

### Example Outputs

#### Outlier Detection Summary
```
Outlier Detection Summary:
Z-Score Method: 150 outliers
IQR Method: 200 outliers
Isolation Forest: 180 outliers
Combined: 250 outliers
Total rows flagged as outliers: 250 out of 10,000
```


### Why This is Important

- **Improved Data Quality:** Removing outliers ensures more reliable and accurate analyses.
- **Enhanced Insights:** Helps identify anomalies that may distort results.
- **Efficiency:** Automates the detection process, saving time and effort.

### Next Steps

1. **Refine Detection Parameters:**
   - Adjust thresholds (e.g., Z-score, IQR multiplier, contamination rate) for better precision.

2. **Handle Detected Outliers:**
   - Investigate flagged data points to decide on removal or correction.

3. **Enhance Visualization:**
   - Add interactive plots for better exploration of outliers.

4. **Expand Functionality:**
   - Include categorical data anomaly detection.
   - Incorporate domain-specific rules for outlier identification.
