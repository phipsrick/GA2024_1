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
    # Initialize the HomeMessagesDB instance with the provided database URL
    db = HomeMessagesDB(dburl)
    
    # Define the timezone for Amsterdam
    amsterdam_tz = pytz.timezone('Europe/Amsterdam')
    
    # Iterate through each provided file
    for file in files:
        # Open each gzip-compressed CSV file in read-text mode
        with gzip.open(file, 'rt') as f:
            # Read the CSV file into a pandas DataFrame
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

            # Convert empty strings to NaN (Not a Number)
            df.replace('', np.nan, inplace=True)

            # Convert NaN values to None (to handle missing values)
            df = df.where(pd.notnull(df), None)

            # Convert the DataFrame to a list of dictionaries, each representing a record
            data = df.to_dict(orient='records')
                
            # Insert the data into the database using the add_p1e method
            db.add_p1e(data)
            
            # Print a confirmation message indicating successful insertion
            print(f"Inserted data from {file} into the database.")

if __name__ == '__main__':
    # Execute the main function when the script is run directly
    main()
