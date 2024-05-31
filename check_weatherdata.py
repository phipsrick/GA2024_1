import click
from sqlalchemy import create_engine, orm
from home_messages_db import WeatherData

@click.command()
@click.option('-d', '--dburl', required=True, help='Database URL')
def check_weather_data(dburl):
    engine = create_engine(dburl)
    with orm.Session(engine) as session:
        try:
            results = session.query(WeatherData).limit(10).all()
            for result in results:
                print(f"ID: {result.id}, Time: {result.time}, Temperature: {result.temperature_2m}, "
                    f"Relative humidity: {result.relativehumidity_2m}, Rain: {result.rain}, Snowfall: {result.snowfall}, "
                    f"Windspeed: {result.windspeed_10m}, Winddirection: {result.winddirection_10m}, Soil temperature: {result.soil_temperature_0_to_7cm}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    check_weather_data()