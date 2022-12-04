from configparser import ConfigParser
from peewee import *
from tkinter import *
from tkinter import filedialog
import psycopg2
import random
from tkinter_choose import tkinter_choose

config = ConfigParser()

config.read('settings.ini')
dbfacts = config['database']

db = PostgresqlDatabase(
    dbfacts['dbname'],
    user=dbfacts['user'],
    password=dbfacts['password'],
    host=dbfacts['host'])

name = tkinter_choose()
print(name)
id = random.randrange(100000000, 999999999)
