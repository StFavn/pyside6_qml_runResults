import os
from app.database.db import Base, engine, session, competitorsModel, timeModel

class DatabaseUtils:
    @staticmethod
    def create_database(engine=engine):
        try:
            Base.metadata.create_all(bind=engine)
            return True, 'База данных создана'
        except Exception as e:
            return False, f'Не удалось создать базу данных: {e}'

    @staticmethod
    def clear_database():
        try:
            Base.metadata.drop_all(bind=engine)
            Base.metadata.create_all(bind=engine)
            return True, 'База данных очищена'
        except Exception as e:
            return False, f'Не удалось очистить базу данных: {e}'
        
    @staticmethod
    def delete_database():
        try:
            os.remove('result.db')
            return True, 'База данных удалена'
        except Exception as e:
            return False, f'Не удалось удалить базу данных: {e}'
    
    @staticmethod
    def save_to_competitorsModel(data: dict):
        try:
            for key, value in data.items():
                competitors = competitorsModel(
                    number=key,
                    name=value['Name'],
                    surname=value['Surname']
                )
                session.add(competitors)
            session.commit()
            return True, 'Данные участников успешно добавлены в базу.'
        except Exception as e:
            session.rollback()
            return False, f'Ошибка: Не удалось добавить данные участников в базу: {e}'
        
    @staticmethod
    def save_to_timesModel(data: dict):
        try:
            for key, value in data.items():
                times = timeModel(
                    number=key,
                    start_time=value['start'],
                    finish_time=value['finish']
                )
                session.add(times)
            session.commit()
            return True, 'Данные забегов успешно добавлены в базу.'
        except Exception as e:
            session.rollback()
            return False, f'Ошибка: Не удалось добавить данные забегов в базу: {e}'
    
    @staticmethod
    def get_competitors():
        return competitorsModel.get_all()
    
    def get_times():
        return timeModel.get_all()