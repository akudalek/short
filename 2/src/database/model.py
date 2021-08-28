# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy import DDL
from sqlalchemy import create_engine
from sqlalchemy import event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.getenvironment import engine_string, schema_db

Base = declarative_base()
event.listen(Base.metadata, 'before_create', DDL(f"CREATE SCHEMA IF NOT EXISTS {schema_db}"))


class Cats(Base):
    """
    Таблица с котами в БД
    """
    __tablename__ = 'cats'
    __table_args__ = {'schema': schema_db}

    id = Column(Integer, primary_key=True)
    name = Column(String)
    breed = Column(String)
    age = Column(Integer)
    description = Column(String)
    img = Column(LargeBinary)


engine = create_engine(engine_string)
Base.metadata.create_all(engine)
Session = sessionmaker(engine)
session = Session()
