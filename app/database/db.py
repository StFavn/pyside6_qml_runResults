from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy import Integer, String
import sqlalchemy.orm

engine = create_engine('sqlite:///result.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = sqlalchemy.orm.declarative_base()

class competitorsModel(Base):
    __tablename__ = 'competitors'

    id = Column(Integer, primary_key=True)
    number = Column(String)
    name = Column(String)
    surname = Column(String)

    def __init__(self, number, name, surname):
        self.number = number
        self.name = name
        self.surname = surname
    
    @classmethod
    def get_all(cls) -> dict:
        competitors = session.query(cls).all()

        data = {}
        for competitor in competitors:
            data[competitor.number] = {
                'name': competitor.name,
                'surname': competitor.surname
            }
        return data
    
    @classmethod
    def get_by_number(cls, number: str) -> dict:
        competitor = session.query(cls).filter_by(number=number).first()
        return {
            'number': competitor.number,
            'name': competitor.name,
            'surname': competitor.surname
        }

class timeModel(Base):
    __tablename__ = 'times'

    id = Column(Integer, primary_key=True)
    number = Column(String)
    start_time = Column(String)
    finish_time = Column(String)

    def __init__(self, number, start_time, finish_time):
        self.number = number
        self.start_time = start_time
        self.finish_time = finish_time
    
    @classmethod
    def get_all(cls) -> list:
        times = session.query(cls).all()
        
        data = []
        for time in times:
            data.append(
                {
                    'number' : time.number,
                    'start_time': time.start_time,
                    'finish_time': time.finish_time
                }
            )
        return data

    @classmethod
    def get_by_number(cls, number: str) -> dict:
        time = session.query(cls).filter_by(number=number).first()
        return {
            'number': time.number,
            'start_time': time.start_time,
            'finish_time': time.finish_time
        }

