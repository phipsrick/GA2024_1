from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import orm 

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
    energy_usage_t1 = Column(Float)
    energy_usage_t2 = Column(Float)

class P1g(Base):
    __tablename__ = 'p1g'
    id = Column(Integer, primary_key=True)
    time = Column(Integer)
    gas_usage = Column(Float)

class HomeMessagesDB:
    pass