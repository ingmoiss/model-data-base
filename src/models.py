import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    User_Id = Column(Integer, primary_key = True)
    Nickname = Column(String(20))
    Password = Column(String(20))
    Name = Column(String(20))
    Last_Name = Column(String(40))
    Birth_Date = Column(Date)

class Characters(Base):
    __tablename__ = 'characters'
    Character_Id = Column(Integer, primary_key = True)
    Name = Column(String(20))
    Birth = Column(Date)
    Gender = Column(String(10))
    Height = Column(Integer) 
    Skin_Color = Column(String(20))
    Eye_Color = Column(String(20))
    Description = Column(String (2000))

class Planets(Base):
    __tablename__ = 'planets'
    Planet_Id = Column(Integer, primary_key = True)
    Name = Column(String(20))
    Climate = Column(String(20))
    Population = Column(Integer)
    Orbital_Period = Column(Integer)
    Rotation_Period = Column(Integer)
    Diamer = Column(Integer)
    Description = Column(String (2000))

class Favorites(Base):
    __tablename__ = 'favorites'
    Fav_Id = Column(Integer, primary_key = True)
    Favorite = Column(String(20))
    User_Id = Column(Integer, ForeignKey('user.User_Id'))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')