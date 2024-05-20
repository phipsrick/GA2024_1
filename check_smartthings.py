import click
from sqlalchemy import create_engine, orm
from home_messages_db import SmartThings

@click.command()
@click.option('-d', '--dburl', required=True, help='Database URL')
def check_smartthings(dburl):
    engine = create_engine(dburl)
    with orm.Session(engine) as session:
        try:
            results = session.query(SmartThings).limit(10).all()
            for result in results:
                print(f"ID: {result.id}, Location: {result.loc}, Level: {result.level}, "
                    f"Name: {result.name}, Epoch: {result.epoch}, Capability: {result.capability}, "
                    f"Attribute: {result.attribute}, Value: {result.value}, Unit: {result.unit}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    check_smartthings()
