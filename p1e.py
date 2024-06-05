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
            # Standardize column names to match database schema
            if 'Electricity imported T1' in df.columns:
                df = df[['time', 'Electricity imported T1', 'Electricity imported T2', 'Electricity exported T1', 'Electricity exported T2']]
                df.columns = ['time', 'electricity_imported_t1', 'electricity_imported_t2', 'electricity_exported_t1', 'electricity_exported_t2']
            elif 'Import T1 kWh' in df.columns:
                df = df[['time', 'Import T1 kWh', 'Import T2 kWh', 'Export T1 kWh', 'Export T2 kWh']]
                df.columns = ['time', 'electricity_imported_t1', 'electricity_imported_t2', 'electricity_exported_t1', 'electricity_exported_t2']
                
            # Convert time to datetime and then to Europe/Amsterdam timezone
            df['time'] = pd.to_datetime(df['time']).dt.tz_localize('UTC').dt.tz_convert(amsterdam_tz).dt.tz_localize(None)

            # Convert empty strings to NaN

            df.replace('', np.nan, inplace=True)

            # Convert NaN to None
            df = df.where(pd.notnull(df), None)

            data = df.to_dict(orient='records')
                
            db.add_p1e(data)
            print(f"Inserted data from {file} into the database.")

if __name__ == '__main__':
    main()
