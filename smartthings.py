import click
from home_messages_db import HomeMessagesDB
import gzip
import pandas as pd

@click.command()
@click.option('-d', '--dburl', required=True, help='Database URL')
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def main(dburl, files):
    # Initialize the HomeMessagesDB instance with the provided database URL
    db = HomeMessagesDB(dburl)
    
    for file in files:
        # Open each gzip-compressed TSV file in read-text mode
        with gzip.open(file, 'rt') as f:
            # Read the TSV file into a pandas DataFrame
            df = pd.read_csv(f, delimiter='\t')
            # Fill any NaN values with empty strings
            df.fillna('', inplace=True)  
            # Convert the DataFrame to a list of dictionaries, each representing a record
            data = df.to_dict(orient='records')
            # Insert the data into the database using the add_smartthings method
            db.add_smartthings(data)  
            # Print a confirmation message indicating successful insertion
            print(f"Inserted data from {file} into the database.")

if __name__ == '__main__':
    # Execute the main function when the script is run directly
    main()
