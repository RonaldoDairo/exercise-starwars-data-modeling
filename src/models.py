import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    ID= Column(Integer, primary_key=True )
    user_name = Column(Integer, unique=True)
    password = Column( String(250))
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250) ,unique=True)


class Planets(Base):
    __tablename__ = 'planets'
    ID= Column(Integer, primary_key=True)
    descripcion = Column(String(250))
    historia = Column(String(250))
    tipos = Column(String(250))

class People(Base):
    __tablename__ = 'people'
    ID= Column(Integer, primary_key=True )
    descripcion = Column(String(250))
    historia = Column(String(250))
    trayectoria = Column(String(250))

class Vehicles(Base):
    __tablename__ = 'vehicles'
    ID= Column(Integer, primary_key=True)
    descripcion = Column(String(250))
    historia = Column(String(250))
    modelo= Column(String(250))

class Favorite(Base):
    __tablename__ = 'favorite'
    ID= Column(Integer, primary_key=True )
    people_id = Column(Integer, ForeignKey('people.ID') )
    people = relationship(People)
    planet_id = Column(Integer , ForeignKey('planets.ID'))
    planet = relationship(Planets)
    vehicle_id = Column(Integer, ForeignKey('vehicles.ID'))
    vehicle = relationship(Vehicles)
    user_id = Column(Integer, ForeignKey('user.ID') )
    user_id_favorite = relationship(User)
    

    

    






    


 

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
