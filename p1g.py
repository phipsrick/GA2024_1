import click
from home_messages_db import HomeMessagesDB
import gzip
import pandas as pd
import pytz

@click.command()
@click.option('-d', '--dburl', required=True, help='Database URL')
@click.argument('files', nargs=-1, type=click.Path(exists=True))

def main(dburl, files):
    db = HomeMessagesDB(dburl)
    amsterdam_tz = pytz.timezone('Europe/Amsterdam')
    
    for file in files:
        with gzip.open(file, 'rt') as f:
            df = pd.read_csv(f, delimiter='\t')
            # Select only the relevant columns
            df = df[['time','Total.gas.used']]
                
            # Convert time to Europe/Amsterdam timezone
            df['time'] = pd.to_datetime(df['time']).dt.tz_localize('UTC').dt.tz_convert(amsterdam_tz)
                
            df.fillna('', inplace=True)  
            data = df.to_dict(orient='records')
            db.add_p1g(data)  
            print(f"Inserted data from {file} into the database.")

if __name__ == '__main__':
    main()