from sqlalchemy import Column, Integer, String, Float, create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.sql import exists 

Base = orm.declarative_base()

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

class P1e(Base):
    __tablename__ = 'p1e'
    id = Column(Integer, primary_key=True)
    time = Column(Integer)
    electricity_imported_t1 = Column(Float)
    electricity_imported_t2= Column(Float)
    electricity_exported_t1 = Column(Float)
    electricity_exported_t2 = Column(Float)  

class P1g(Base):
    __tablename__ = 'p1g'
    id = Column(Integer, primary_key=True)
    time = Column(Integer)
    total_gas_used = Column(Float)

class WeatherData(Base):
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True)
    time = Column(Integer, index=True) 
    temperature_2m = Column(Float)
    relativehumidity_2m = Column(Float)
    rain_mm = Column(Float)
    snowfall_cm = Column(Float)
    windspeed_10m = Column(Float)
    winddirection_10m = Column(Float)
    soil_temperature_0_to_7cm = Column(Float)

class HomeMessagesDB:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)

    def add_smartthings(self, data):
        with orm.Session(self.engine) as session:
            try:
                for record in data:
                    exists_query = session.query(exists().where(
                        SmartThings.loc == record['loc']).where(
                        SmartThings.level == record['level']).where(
                        SmartThings.name == record['name']).where(
                        SmartThings.epoch == record['epoch'])).scalar()
                    if not exists_query:
                        session.add(SmartThings(**record))
                session.commit()
            except Exception as e:
                session.rollback()
                raise Exception(f"Error inserting SmartThings data: {e}")

    def add_p1e(self, data):
        with orm.Session(self.engine) as session:
            try:
                for record in data:
                    exists_query = session.query(exists().where(
                        P1e.time == record['time'])).scalar()
                    if not exists_query:
                        session.add(P1e(**record))
                session.commit()
            except Exception as e:
                session.rollback()
                raise Exception(f"Error inserting P1e data: {e}")

    def add_p1g(self, data):
        with orm.Session(self.engine) as session:
            try:
                for record in data:
                    exists_query = session.query(exists().where(
                        P1g.time == record['time'])).scalar()
                    if not exists_query:
                        session.add(P1g(**record))
                session.commit()
            except Exception as e:
                session.rollback()
                raise Exception(f"Error inserting P1g data: {e}")
    
    def add_weather_data(self, data):
        with orm.Session(self.engine) as session:
            try:
                for record in data:
                    exists_query = session.query(exists().where(
                        WeatherData.time == record['time'])).scalar()
                    if not exists_query:
                        session.add(WeatherData(**record))
                session.commit() 
            except Exception as e:
                session.rollback() 
                raise Exception(f"Error inserting weather data: {e}")