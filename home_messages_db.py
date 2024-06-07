from sqlalchemy import Column, Integer, String, Float, create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.sql import exists 
import pandas as pd

# Define the base class for declarative class definitions
Base = orm.declarative_base()

# Define the SmartThings table structure
class SmartThings(Base):
    __tablename__ = 'smartthings'
    id = Column(Integer, primary_key=True)
    loc = Column(String)
    level = Column(String)
    name = Column(String)
    epoch = Column(Integer)
    capability = Column(String)
    attribute = Column(String)
    value = Column(String)
    unit = Column(String)

# Define the P1e table structure
class P1e(Base):
    __tablename__ = 'p1e'
    id = Column(Integer, primary_key=True)
    time = Column(Integer, unique=True)
    electricity_imported_t1 = Column(Float)
    electricity_imported_t2 = Column(Float)
    electricity_exported_t1 = Column(Float)
    electricity_exported_t2 = Column(Float)  

# Define the P1g table structure
class P1g(Base):
    __tablename__ = 'p1g'
    id = Column(Integer, primary_key=True)
    time = Column(Integer, unique=True)
    total_gas_used = Column(Float)

# Define the WeatherData table structure
class WeatherData(Base):
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True)
    time = Column(Integer, index=True) 
    temperature_2m = Column(Float)
    relativehumidity_2m = Column(Float)
    rain = Column(Float)
    snowfall = Column(Float)
    windspeed_10m = Column(Float)
    winddirection_10m = Column(Float)
    soil_temperature_0_to_7cm = Column(Float)

# Define the HomeMessagesDB class for database operations
class HomeMessagesDB:
    def __init__(self, db_url):
        # Initialize the database engine and create tables if they don't exist
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    # Method to add SmartThings data to the database
    def add_smartthings(self, data):
        with orm.Session(self.engine) as session:
            try:
                # Check for existing records to avoid duplicates
                existing_records = session.query(SmartThings.loc, SmartThings.level, SmartThings.name, SmartThings.epoch).all()
                existing_records_set = set(existing_records)

                # Filter out new records that are not already in the database
                new_records = [SmartThings(**record) for record in data if (
                    record['loc'], record['level'], record['name'], record['epoch']) not in existing_records_set]

                # Bulk insert new records
                session.bulk_save_objects(new_records)
                session.commit()
            except Exception as e:
                session.rollback()
                raise Exception(f"Error inserting SmartThings data: {e}")

    # Method to add P1e data to the database
    def add_p1e(self, records):
        with orm.Session(self.engine) as session:
            try:
                for record in records:
                    # Convert timestamp to string format
                    record['time'] = str(record['time'])
                    # Check if the record already exists to avoid duplicates
                    if not session.query(P1e).filter(P1e.time == record['time']).scalar():
                        p1e = P1e(**record)
                        session.add(p1e)
                session.commit()
            except Exception as e:
                session.rollback()
                raise Exception(f"Error inserting P1e data: {e}")

    # Method to add P1g data to the database
    def add_p1g(self, records):
        with orm.Session(self.engine) as session:
            try:
                for record in records:
                    # Convert timestamp to string format
                    record['time'] = str(record['time'])
                    # Check if the record already exists to avoid duplicates
                    if not session.query(P1g).filter(P1g.time == record['time']).scalar():
                        p1g = P1g(**record)
                        session.add(p1g)
                session.commit()
            except Exception as e:
                session.rollback()
                raise Exception(f"Error inserting P1g data: {e}")
    
    # Method to add weather data to the database
    def add_weather_data(self, data):
        with orm.Session(self.engine) as session:
            try:
                for record in data:
                    # Check if the record already exists to avoid duplicates
                    exists_query = session.query(exists().where(
                        WeatherData.time == record['time'])).scalar()
                    if not exists_query:
                        session.add(WeatherData(**record))
                session.commit() 
            except Exception as e:
                session.rollback() 
                raise Exception(f"Error inserting weather data: {e}")

    # Method to retrieve SmartThings data from the database
    def get_smartthings(self):
        with orm.Session(self.engine) as session:
            query = session.query(SmartThings).all()
        data = [(row.id, row.loc, row.level, row.name, row.epoch, row.capability, row.attribute, row.value, row.unit) for row in query]
        df = pd.DataFrame(data, columns=['id', 'loc', 'level', 'name', 'epoch', 'capability', 'attribute', 'value', 'unit'])
        return df

    # Method to retrieve P1e data from the database
    def get_p1e(self):
        with orm.Session(self.engine) as session:
            query = session.query(P1e).all()
        data = [(row.id, row.time, row.electricity_imported_t1, row.electricity_imported_t2, row.electricity_exported_t1, row.electricity_exported_t2) for row in query]
        df = pd.DataFrame(data, columns=['id', 'time', 'electricity_imported_t1', 'electricity_imported_t2', 'electricity_exported_t1', 'electricity_exported_t2'])
        return df

    # Method to retrieve P1g data from the database
    def get_p1g(self):
        with orm.Session(self.engine) as session:
            query = session.query(P1g).all()
        data = [(row.id, row.time, row.total_gas_used) for row in query]
        df = pd.DataFrame(data, columns=['id', 'time', 'total_gas_used'])
        return df

    # Method to retrieve weather data from the database
    def get_weather_data(self):
        with orm.Session(self.engine) as session:
            query = session.query(WeatherData).all()
        data = [(row.id, row.time, row.temperature_2m, row.relativehumidity_2m, row.rain, row.snowfall, row.windspeed_10m, row.winddirection_10m, row.soil_temperature_0_to_7cm) for row in query]
        df = pd.DataFrame(data, columns=['id', 'time', 'temperature_2m', 'relativehumidity_2m', 'rain', 'snowfall', 'windspeed_10m', 'winddirection_10m', 'soil_temperature_0_to_7cm'])
        return df
