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

## Report Description

### `report_temperature_and_motion.ipynb`

This report analyzes the relationship between motion sensor events and weather conditions on weekends. The data is sourced from SmartThings sensors and weather data, which are merged and analyzed to understand the impact of temperature and rain on motion events inside the house. The analysis includes:

- **Data Preparation**: Conversion of epoch times to datetime formats, identification of weekends, filtering for relevant motion sensor events, and merging with weather data.
- **Descriptive Statistics**: Calculation of descriptive statistics for key weather variables and motion events.
- **Distribution Analysis**: Examination of the distribution of motion events using histograms, chi-squared tests, and normality tests.
- **Regression Analysis**: Performing a Negative Binomial regression to explore the relationship between motion counts and weather variables.
- **Visualization**: Scatter plots and regression lines to visually represent the relationships identified in the analysis.

The report concludes that temperature has a statistically significant negative relationship with motion events, while rain does not significantly affect the number of motion events.

### `report2.ipynb`
xxx

### `report3.ipynb`
xxx
{## Open Meteo weather tool (openweathermap.py)

This tool downloads historical weather data from January 2022 up to April 2024 from the region of interest (Nordwijk area) through an API provided by open-meteo.com. and loads it into the database by processing the downloaded json file. 

The Historical Weather API is based on reanalysis datasets and uses a combination of weather station, aircraft, buoy, radar, and satellite observations to create a comprehensive record of past weather conditions. These datasets are able to fill in gaps by using mathematical models to estimate the values of various weather variables. The models for historical weather data use a spatial resolution of 9 km. 

Covered weather variables from the region of interest include a timestamp, the air temperature at 2 meters above ground in °C units (temperature_2m), the relative humidity at 2 meters above ground in % units (relativehumidity_2m), the liquid precipitation of the preceding hour including local showers and rain from large scale systems in mm units (rain), the snowfall amount of the preceding hour in cm units (snowfall), the wind speed at 10 meters above ground in km/h units (windspeed_10m), the wind direction at 10 meters above ground in °degree units (winddirection_10m), and the average temperature of the soil 7cm below ground in °C units(soil_temperature_0_to_7cm).}

## Contributions
Josh 
Magda
Maria
Myrto
Philipp





