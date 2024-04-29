import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Date, Float, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    subscription_date = Column(DateTime)
    first_name = Column(String(50))
    last_name = Column(String(50))
    favorites = relationship("Favorite", back_populates="user") 

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(50))
    eye_color = Column(String(50))
    gender = Column(String(50))
    hair_color = Column(String(50))
    height = Column(String(50))
    mass = Column(String(50))
    skin_color = Column(String(50))
    favorites = relationship("Favorite", back_populates="people")  

class Film(Base):
    __tablename__ = 'film'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    director = Column(String(250))
    episode_id = Column(Integer)
    opening_crawl = Column(Text)
    producer = Column(String(250))
    release_date = Column(Date)
    favorites = relationship("Favorite", back_populates="film")  


class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    starship_class = Column(String(250))
    manufacturer = Column(String(250))
    length = Column(String(50))
    crew = Column(String(50))
    passengers = Column(String(50))
    cargo_capacity = Column(String(50))
    consumables = Column(String(50))
    hyperdrive_rating = Column(Float)
    MGLT = Column(String(50))
    max_atmosphering_speed = Column(String(50))
    cost_in_credits = Column(String(50))
    favorites = relationship("Favorite", back_populates="starship")  


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    vehicle_class = Column(String(250))
    manufacturer = Column(String(250))
    length = Column(Float)
    crew = Column(String(50))
    passengers = Column(String(50))
    cargo_capacity = Column(String(50))
    consumables = Column(String(50))
    max_atmosphering_speed = Column(String(50))
    cost_in_credits = Column(String(50))
    favorites = relationship("Favorite", back_populates="vehicle")  


class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    classification = Column(String(250))
    designation = Column(String(250))
    average_height = Column(Float)
    average_lifespan = Column(Integer)
    eye_colors = Column(String(250))
    hair_colors = Column(String(250))
    skin_colors = Column(String(250))
    language = Column(String(250))
    favorites = relationship("Favorite", back_populates="species")  


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    diameter = Column(Integer)
    gravity = Column(String(50))
    orbital_period = Column(Integer)
    population = Column(Integer)
    rotation_period = Column(Integer)
    surface_water = Column(Integer)
    terrain = Column(String(250))
    favorites = relationship("Favorite", back_populates="planet")   


class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key = True)
    item_class = Column(String(50), nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'), nullable = False)
    user = relationship("User", back_populates="favorites")
    people_id = Column(Integer, ForeignKey('people.id'))
    people = relationship("People", back_populates="favorites")  
    film_id = Column(Integer, ForeignKey('film.id'))
    film = relationship("Film", back_populates="favorites") 
    starship_id = Column(Integer, ForeignKey('starship.id'))
    starship = relationship("Starship", back_populates="favorites")  
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    vehicle = relationship("Vehicle", back_populates="favorites") 
    species_id = Column(Integer, ForeignKey('species.id'))
    species = relationship("Species", back_populates="favorites")
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship("Planet", back_populates="favorites")



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
