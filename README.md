# GA2024_1: Smart Home Energy and Weather Data Analysis
Essentials for Data Science Group Assignment

## Overview

This project aims to analyze energy and weather data collected from various smart home devices and external weather sources. The data, spanning over 19 months, originates from a single-family home in Nordwijk, NL, and includes readings from smart home devices such as power/gas meters, wall sockets, switches, light bulbs, temperature/humidity sensors, and more. The main goals of the project are to store the data in a relational database, process and analyze it to gain insights into energy usage patterns, and explore the relationship between environmental factors and smart home device activities.

## Files

- `home_messages_db.py`: Database access module.
- `smartthings.py`: Command-line tool to insert SmartThings data into the database.
- `p1e.py`: Command-line tool to insert electricity usage data into the database.
- `p1g.py`: Command-line tool to insert gas usage data into the database.
- `openweathermap.py`: Command-line tool to fetch and insert weather data into the database.
- `report_temperature_and_motion.ipynb`: Analyzes the relationship between motion sensor events and weather conditions on weekends. The report includes descriptive statistics, distribution analysis, regression analysis, and visualization of motion events against temperature and rain.
- `report2.ipynb`: Notebook analyzing xxx.
- `report3.ipynb`: Notebook analyzing xxx.

## Setup and Usage

### Prerequisites

- Python 
- Required Python packages can be found in requirements.txt

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/GA2024_1.git
   cd GA2024_1
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Initialize the database and insert data:
    ```bash
    python smartthings.py -d sqlite:///myhome.db Data/smartthings/smartthings.*
    python p1e.py -d sqlite:///myhome.db Data/P1e/P1e-*.csv.gz
    python p1g.py -d sqlite:///myhome.db Data/P1g/P1g-*.csv.gz
    python openweathermap.py -d sqlite:///myhome.db
    ```

4. Run the analysis notebooks:
    Open each notebook in Jupyter and run all cells to generate the analyses and visualizations.

    ```bash
    jupyter notebook report_temperature_and_motion.ipynb
    jupyter notebook report2.ipynb
    jupyter notebook report3.ipynb
    ```
## Tool Descriptions 

### `smartthings.py`
This tool processes and loads smart home device data from SmartThings into the database. It reads compressed TSV files containing messages from various smart home devices. The tool converts these messages into a standardized format by handling missing values and ensuring unique records. It maps columns like location, level, name, and timestamp to the database schema and ensures that no duplicate records are inserted. A confirmation message is printed after successfully inserting data from each file.

### `p1e.py`
This tool processes and loads electricity consumption data into the database. It reads compressed CSV files containing electricity usage data collected biweekly with a 15-minute resolution. The tool standardizes column names to match the database schema, converts timestamps to the Europe/Amsterdam timezone, and handles missing values by replacing empty strings with NaN. It ensures no duplicate records are inserted, maintaining data integrity, and prints a confirmation message upon successful data insertion.

### `p1g.py`
This tool processes and loads gas consumption data into the database. It reads compressed CSV files containing gas usage data collected biweekly with a 15-minute resolution. The tool standardizes column names to match the database schema, converts timestamps to the Europe/Amsterdam timezone, and handles missing values by replacing empty strings with NaN. It ensures no duplicate records are inserted, maintaining data integrity, and prints a confirmation message upon successful data insertion.

### `openweathermap.py` 
This tool downloads historical weather data from January 2022 up to April 2024 for the Nordwijk area through an API provided by open-meteo.com and loads it into the database by processing the downloaded JSON file. The Historical Weather API uses reanalysis datasets combining weather station, aircraft, buoy, radar, and satellite observations to create a comprehensive record of past weather conditions. Weather variables include air temperature at 2 meters, relative humidity at 2 meters, precipitation, snowfall, wind speed at 10 meters, wind direction at 10 meters, and soil temperature at 7 cm below ground. The tool handles data gaps using mathematical models and ensures accurate data insertion.

## Report Descriptions

### `report_temperature_and_motion.ipynb`

This report analyzes the relationship between motion sensor events and weather conditions on weekends. The data is sourced from SmartThings sensors and weather data, which are merged and analyzed to understand the impact of temperature and rain on motion events inside the house. The analysis includes:

- **Data Preparation**: Conversion of epoch times to datetime formats, identification of weekends, filtering for relevant motion sensor events, and merging with weather data.
- **Descriptive Statistics**: Calculation of descriptive statistics for key weather variables and motion events.
- **Distribution Analysis**: Examination of the distribution of motion events using histograms, chi-squared tests, and normality tests.
- **Regression Analysis**: Performing a Negative Binomial regression to explore the relationship between motion counts and weather variables.
- **Visualization**: Scatter plots and regression lines to visually represent the relationships identified in the analysis.

The report concludes that temperature has a statistically significant negative relationship with motion events, while rain does not significantly affect the number of motion events.

### `report_temperature_gas_usage.ipynb`

This report analyzes the relationship between in-house temperature and outside temperature in the Nordwijk area and the households' daily gas usage. Inside temperature is sourced from Smartthings, outside temperature is taken from the weather data, and gas usage is taken from the gas usage data (P1g). This report provides data preprocessing, summary statistics, time-series visualizations, correlation and regression analyses. 

We could conclude that there is a slight positive association between inside temperature and daily gas usage and heavy negative correlation between outside temperature and gas usage. Household members use less gas in the cold periods than in the warm periods.


### `report3.ipynb`
xxx


## Contributions
| Full Name        | Student Number | GitHub Name  |
|-----------------|--------|-------------|
| Joshua Damm       | s4036018    | SensationSeeker    | 
| Magda      | xxx    | xxx    |
| Maria      | xxx    | xxx    | 
| Myrto      | xxx    | xxx    | 
| Philipp Rickert | s2487632 | phipsrick |

We declare that all group members contributed equally to all project tasks so that we receive a group grade instead of individual grades.
