# GA2024_1
Essentials for Data Science Group Assignment

# Open Meteo weather tool (openweathermap.py)

This tool downloads historical weather data from January 2022 up to April 2024 from the region of interest (Nordwijk area) through an API provided by open-meteo.com. and loads it into the database by processing the downloaded json file. 

The Historical Weather API is based on reanalysis datasets and uses a combination of weather station, aircraft, buoy, radar, and satellite observations to create a comprehensive record of past weather conditions. These datasets are able to fill in gaps by using mathematical models to estimate the values of various weather variables. The models for historical weather data use a spatial resolution of 9 km. 

Covered weather variables from the region of interest include a timestamp, the air temperature at 2 meters above ground in °C units (temperature_2m), the relative humidity at 2 meters above ground in % units (relativehumidity_2m), the liquid precipitation of the preceding hour including local showers and rain from large scale systems in mm units (rain), the snowfall amount of the preceding hour in cm units (snowfall), the wind speed at 10 meters above ground in km/h units (windspeed_10m), the wind direction at 10 meters above ground in °degree units (winddirection_10m), and the average temperature of the soil 7cm below ground in °C units(soil_temperature_0_to_7cm).



