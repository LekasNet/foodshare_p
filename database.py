import sys
# для настройки баз данных
from sqlalchemy import Column, ForeignKey, Integer, String

# для определения таблицы и модели
from sqlalchemy.ext.declarative import declarative_base

# для создания отношений между таблицами
from sqlalchemy.orm import relationship

# для настроек
from sqlalchemy import create_engine

# создание экземпляра declarative_base
Base = declarative_base()

# здесь добавим классы

# создает экземпляр create_engine в конце файла
engine = create_engine('sqlite:///FoodShare.db')

Base.metadata.create_all(engine)


class Foodshare(Base):
    __tablename__ = 'foodsharing'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    contacts = Column(String(250))
    image = Column(String(250))
    price = Column(Integer)
    confirmed = Column(String(250))