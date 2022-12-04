from start import *
from data_table import *
import csv
from csv_table import *
from add import *

db.connect()
try:
    cur.execute('''CREATE TABLE DATA
            (
            id BIGINT PRIMARY KEY NOT NULL,
            path TEXT UNIQUE,
            last_use TEXT);''')
except:
    pass
cur.execute("COMMIT")
add()
