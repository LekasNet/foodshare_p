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

    ID = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False)
    Description = Column(String(250), nullable=False)
    Image = Column(String(250))
    Price = Column(Integer)
    Confirmed = Column(String(250))
