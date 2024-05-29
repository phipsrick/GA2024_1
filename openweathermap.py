import click
from home_messages_db import HomeMessagesDB
import pandas as pd
import requests

@click.command()
@click.option('-d', '--dburl', required=True, help='Database URL')
def main(dburl):
    url = "https://archive-api.open-meteo.com/v1/era5?latitude=52.19&longitude=4.44&timeformat=unixtime&start_date=2022-01-01&end_date=2024-04-30&hourly=temperature_2m,relativehumidity_2m,rain,snowfall,windspeed_10m,winddirection_10m,soil_temperature_0_to_7cm"
    download = requests.get(url)
    if download.status_code == 200:
        data = download.json()
        weather_data = pd.DataFrame(data['hourly'])
        weather_data.fillna('', inplace=True) 
        weather_data_records = weather_data.to_dict(orient='records')

        db = HomeMessagesDB(dburl)
        db.add_weather_data(weather_data_records)
        print(f"Inserted data from Open Meteo into the database.")
    else:
        print("Failed to retrieve data.")

if __name__ == '__main__':
    main()