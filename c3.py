from datetime import date
from datetime import datetime
from pony.orm import *


db = Database()


class Movie(db.Entity):
    id = PrimaryKey(int, auto=True)
    genre = Required('Genre')
    age_rating = Required('Age_rating')
    dvds = Set('Dvd')
    name = Optional(str)
    lenth = Optional(int)
    description = Optional(LongStr)
    posta = Optional(str)
    year_of_release = Optional(date)


class Customer(db.Entity):
    id = PrimaryKey(int, auto=True)
    firstname = Optional(str)
    lastname = Optional(str)
    phone = Optional(str)
    email = Optional(str)
    address = Optional(LongStr)
    family = Optional(str)
    blacklisted = Optional(bool)
    cus_dvds = Set('Cus_dvd')


class Shelve(db.Entity):
    id = PrimaryKey(int, auto=True)
    dvds = Set('Dvd')
    racks = Optional(int)
    max_capacity = Optional(int)


class Genre(db.Entity):
    id = PrimaryKey(int, auto=True)
    movies = Set(Movie)
    name = Optional(str)
    description = Optional(LongStr)


class Age_rating(db.Entity):
    movies = Set(Movie)
    name = Optional(str)
    min_age = Optional(int)


class Dvd(db.Entity):
    id = PrimaryKey(int, auto=True)
    movie = Required(Movie)
    shelve = Required(Shelve)
    cus_dvds = Set('Cus_dvd')


class Cus_dvd(db.Entity):
    customers = Required(Customer)
    dvds = Required(Dvd)
    date_in = Optional(datetime)
    date_out = Optional(datetime)
    lent_out = Optional(bool)
    PrimaryKey(customers, dvds)


db.bind("postgres", hosts="localhost", user="samuel", database="samuel", password="password")
db.generate_mapping(create_tables = True)

