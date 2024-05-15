import click
from home_messages_db import HomeMessagesDB
import gzip
import pandas as pd

@click.command()
@click.option('-d', '--dburl', required=True, help='Database URL')
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def main(dburl, files):
    db = HomeMessagesDB(dburl)
    
    for file in files:
        with gzip.open(file, 'rt') as f:
            df = pd.read_csv(f, delimiter='\t')
            df.fillna('', inplace=True)  
            data = df.to_dict(orient='records')
            db.add_smartthings(data)  
            print(f"Inserted data from {file} into the database.")

if __name__ == '__main__':
    main()
