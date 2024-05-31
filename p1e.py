import click
from home_messages_db import HomeMessagesDB
import pandas as pd
import gzip
import pytz

@click.command()
@click.option('-d', '--dburl', required=True, help='Database URL')
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def main(dburl, files):
    db = HomeMessagesDB(dburl)
    amsterdam_tz = pytz.timezone('Europe/Amsterdam')
    
    for file in files:
        if file.startswith('P1e-'):
            with gzip.open(file, 'rt') as f:
                df = pd.read_csv(f)
                # Select only the relevant columns
                df = df[['time', 'Electricity imported T1', 'Electricity imported T2', 'Electricity exported T1', 'Electricity exported T2']]
                df.columns = ['time', 't1_imported', 't2_imported', 't1_exported', 't2_exported']
                
                # Convert time to Europe/Amsterdam timezone
                df['time'] = pd.to_datetime(df['time']).dt.tz_localize('UTC').dt.tz_convert(amsterdam_tz)
                
                df.fillna('', inplace=True)
                data = df.to_dict(orient='records')
                
                db.add_p1e(data)
                print(f"Inserted data from {file} into the database.")
        else:
            print(f"Skipped file {file} as it does not start with 'P1e-'")

if __name__ == '__main__':
    main()
