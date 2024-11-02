# PVDH-Projekti
 Projekti nga lënda "Përgatitja dhe vizualizimi i të dhënave"


Mbledhja e të dhënave

Për mbledhjen e të dhënave për datasetin World Economic Indicators, janë përdorur burime të ndryshme të besueshme që përfshijnë të dhënat nga Banka Botërore dhe Indeksi i Zhvillimit Njerëzor (HDI) nga Kombet e Bashkuara (UN). Të dhënat e Bankës Botërore mbulojnë periudhën nga viti 1960 deri në 2018 dhe përfshijnë tregues të ndryshëm ekonomikë dhe të zhvillimit, si konsumi i energjisë elektrike, GDP për frymë, jetëgjatësia, dhe shumë të tjera.
Për të shtuar më shumë informacion mbi zhvillimin social dhe ekonomik të vendeve, janë përfshirë të dhëna nga HDI, të cilat përfshijnë tregues të tjerë të lidhur me jetëgjatësinë, GDP për frymë, dhe arritjet në arsim për çdo vend nga viti 1990 deri në 2021. Këto të dhëna u përdorën për të ndjekur zhvillimin, ndikimin mjedisor, dhe pabarazinë në vendet e ndryshme.
Pasi të dhënat janë të ndara në 3 tabela me 12,657 rekorde gjithsej dhe 58 fusha, është e rëndësishme të strukturohen dhe të përgatiten në mënyrë të tillë që të lehtësohet analizimi i tyre. Të dhënat përfshijnë variabla kohorë dhe hapësinorë, të cilat ndihmojnë për të ndjekur ndryshimet gjatë viteve në vende të ndryshme.
Ky proces i mbledhjes së të dhënave synon të sigurojë një pamje gjithëpërfshirëse të treguesve ekonomikë dhe socialë për zhvillimin global, duke krijuar mundësinë për të analizuar rritjen ekonomike, përmirësimet në shëndetësi dhe arsim, si dhe diferencat midis vendeve me të ardhura të larta dhe të ulëta.



Definimi i tipeve të të dhënave


| Table     | Field                                                           | Data Type | Description                                                                                                 |
|-----------|-----------------------------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------|
| WorldBank | Country Name                                                    | String    | The name of the country                                                                                     |
| WorldBank | Country Code                                                    | String    | The three-letter code representing the country                                                              |
| WorldBank | Region                                                          | String    | The World Bank region of the country                                                                        |
| WorldBank | IncomeGroup                                                     | String    | The World Bank Income Group of the country                                                                  |
| WorldBank | Year                                                            | Integer   | The Year in which the statistics were recorded                                                              |
| WorldBank | Birth rate, crude (per 1,000 people)                            | Float     | The Birth rate per 1000 people in the country                                                               |
| WorldBank | Death rate, crude (per 1,000 people)                            | Float     | The death rate per 1000 people in the country                                                               |
| WorldBank | Electric power consumption (kWh per capita)                     | Float     | The electricity consumption per person in kilowatt-hours in the country                                     |
| WorldBank | GDP (USD)                                                       | Float     | The gross domestic product, or total economic output of the country                                         |
| WorldBank | GDP per capita (USD)                                            | Float     | The gross domestic product, or economic output per person in the country                                    |
| WorldBank | Individuals using the Internet (% of population)                | Float     | The percentage of individuals using the internet in each country                                            |
| WorldBank | Infant mortality rate (per 1,000 live births)                   | Float     | The infant mortality rate per 1000 births in the country                                                    |
| WorldBank | Life expectancy at birth (years)                                | Float     | The life expectancy in years at birth in the country                                                        |
| WorldBank | Population density (people per sq. km of land area)             | Float     | The number of people per square kilometer in the country                                                    |
| WorldBank | Unemployment (% of total labor force) (modeled ILO estimate)    | Float     | The percentage of the labor force that is not employed                                                      |
| hdi       | iso3                                                            | String    | The three-letter code representing the country                                                              |
| hdi       | country                                                         | String    | The name of the country                                                                                     |
| hdi       | hdicode                                                         | String    | The HDI grouping from the UN                                                                                |
| hdi       | region                                                          | String    | The UNDP development regions                                                                                |
| hdi       | hdi_rank_2021                                                   | Integer   | The country's HDI rank in 2021                                                                              |
| hdi       | hdi_xxxx                                                        | Float     | The country's HDI in year xxxx                                                                              |
| hdi       | le_xxxx                                                         | Float     | The country's life expectancy in year xxxx                                                                  |
| hdi       | eys_xxxx                                                        | Float     | The country's expected years of schooling                                                                   |
| hdi       | mys_xxxx                                                        | Float     | The country's mean years of schooling                                                                       |
| hdi       | gnipc_xxxx                                                      | Float     | The gross national income per capita in 2017 PPP dollars                                                    |
| hdi       | gdi_group_2021                                                  | String    | The Gender Development Group                                                                                |
| hdi       | gdi_xxxx                                                        | Float     | Gender Development Index in year xxxx                                                                       |
| hdi       | hdi_f_xxxx                                                      | Float     | Female HDI in year xxxx                                                                                     |
| hdi       | le_f_xxxx                                                       | Float     | Female life expectancy at birth in year xxxx                                                                |
| hdi       | eys_f_xxxx                                                      | Float     | Female expected years of schooling in year xxxx                                                             |
| hdi       | mys_f_xxxx                                                      | Float     | Female mean years of schooling in year xxxx                                                                 |
| hdi       | gni_pc_f_xxxx                                                   | Float     | Female GNI per capita in year xxxx                                                                          |
| hdi       | hdi_m_xxxx                                                      | Float     | Male HDI in year xxxx                                                                                       |
| hdi       | le_m_xxxx                                                       | Float     | Male life expectancy at birth in year xxxx                                                                  |
| hdi       | eys_m_xxxx                                                      | Float     | Male expected years of schooling in year xxxx                                                               |
| hdi       | mys_m_xxxx                                                      | Float     | Male mean years of schooling in year xxxx                                                                   |
| hdi       | gni_pc_m_xxxx                                                   | Float     | Male GNI per capita in year xxxx                                                                            |
| hdi       | ihdi_xxxx                                                       | Float     | Inequality Adjusted HDI in year xxxx                                                                        |
| hdi       | coef_ineq_xxxx                                                  | Float     | Coefficient of human inequality in year xxxx                                                                |
| hdi       | loss_xxxx                                                       | Float     | Overall loss (%) in year xxxx                                                                               |
| hdi       | ineq_le_xxxx                                                    | Float     | Inequality in life expectancy in year xxxx                                                                  |
| hdi       | ineq_edu_xxxx                                                   | Float     | Inequality in education in year xxxx                                                                        |
| hdi       | ineq_inc_xxxx                                                   | Float     | Inequality in income in year xxxx                                                                           |
| hdi       | gii_rank_2021                                                   | Integer   | Gender Inequality index rank in 2021                                                                        |
| hdi       | gii_xxxx                                                        | Float     | Gender inequality index in year xxxx                                                                        |
| hdi       | mmr_xxxx                                                        | Float     | Maternal Mortality Ratio (deaths per 100,000 live births) in year xxxx                                      |
| hdi       | abr_xxxx                                                        | Float     | Adolescent birth rate (births per 1000 women aged 15-19) in year xxxx                                       |
| hdi       | se_f_xxxx                                                       | Float     | Population with at least some secondary education, female (% ages 25 and older) in year xxxx               |
| hdi       | se_m_xxxx                                                       | Float     | Population with at least some secondary education, male (% ages 25 and older) in year xxxx                 |
| hdi       | pr_f_xxxx                                                       | Float     | Share of seats in parliament, female (% held by women) in year xxxx                                        |
| hdi       | pr_m_xxxx                                                       | Float     | Share of seats in parliament, male (% held by men) in year xxxx                                            |
| hdi       | lfpr_f_xxxx                                                     | Float     | Labour force participation rate, female (% ages 15 and older) in year xxxx                                 |
| hdi       | lfpr_m_xxxx                                                     | Float     | Labour force participation rate, male (% ages 15 and older) in year xxxx                                   |
| hdi       | rankdiff_hdi_phdi_2021                                          | Integer   | Difference in HDI rank from 2020                                                                            |
| hdi       | phdi_xxxx                                                       | Float     | Planetary pressures-adjusted Human Development Index (value) in year xxxx                                  |
| hdi       | diff_hdi_phdi_xxxx                                              | Float     | Difference from HDI value (%) in year xxxx                                                                  |
| hdi       | co2_prod_xxxx                                                   | Float     | Carbon dioxide emissions per capita (production) (tonnes) in year xxxx                                      |
| hdi       | mf_xxxx                                                         | Float     | Material footprint per capita (tonnes) in year xxxx                                                        |
