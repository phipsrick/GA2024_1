import click
from home_messages_db import HomeMessagesDB
import pandas as pd
import numpy as np
import gzip
import pytz

@click.command()
@click.option('-d', '--dburl', required=True, help='Database URL')
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def main(dburl, files):
    db = HomeMessagesDB(dburl)
    amsterdam_tz = pytz.timezone('Europe/Amsterdam')
    
    for file in files:
        with gzip.open(file, 'rt') as f:
            df = pd.read_csv(f)

            # Convert time to datetime and then to Europe/Amsterdam timezone
            df['time'] = pd.to_datetime(df['time']).dt.tz_localize('UTC').dt.tz_convert(amsterdam_tz).dt.tz_localize(None)
            
            # Debugging: Print final time column
            #print("Final 'time' column after timezone conversion:")
            #print(df['time'].head())

            # Convert empty strings to NaN

            df.replace('', np.nan, inplace=True)

            # Convert NaN to None
            df = df.where(pd.notnull(df), None)

            data = df.to_dict(orient='records')
                
            db.add_p1g(data)
            print(f"Inserted data from {file} into the database.")

if __name__ == '__main__':
    main()
