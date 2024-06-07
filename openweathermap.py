import click
from home_messages_db import HomeMessagesDB
import pandas as pd
import requests

@click.command()
@click.option('-d', '--dburl', required=True, help='Database URL')
def main(dburl):
    # Initialize the HomeMessagesDB instance with the provided database URL
    db = HomeMessagesDB(dburl)
    
    # URL to fetch weather data from Open Meteo API
    url = "https://archive-api.open-meteo.com/v1/era5?latitude=52.19&longitude=4.44&timeformat=unixtime&start_date=2022-01-01&end_date=2024-04-30&hourly=temperature_2m,relativehumidity_2m,rain,snowfall,windspeed_10m,winddirection_10m,soil_temperature_0_to_7cm"
    
    # Send a GET request to the API
    download = requests.get(url)
    
    # Check if the request was successful
    if download.status_code == 200:
        # Parse the JSON response
        data = download.json()
        
        # Convert the 'hourly' data to a pandas DataFrame
        df = pd.DataFrame(data['hourly'])
        
        # Fill any NaN values with empty strings
        df.fillna('', inplace=True)
        
        # Convert the DataFrame to a list of dictionaries, each representing a record
        data = df.to_dict(orient='records')
        
        # Insert the data into the database using the add_weather_data method
        db.add_weather_data(data)
        
        # Print a confirmation message indicating successful insertion
        print(f"Inserted data from Open Meteo into the database.")
    else:
        # Print an error message if the data retrieval failed
        print("Failed to retrieve data.")

if __name__ == '__main__':
    # Execute the main function when the script is run directly
    main()
