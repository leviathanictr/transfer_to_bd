from start import *
con = psycopg2.connect(dbname=dbfacts['dbname'], user=dbfacts['user'],
                       password=dbfacts['password'], host=dbfacts['host'])

cur = con.cursor()
start_name = name[0]

def Data_create():
    cur.execute('''CREATE TABLE DATA
            (
            id BIGINT PRIMARY KEY NOT NULL,
            path TEXT UNIQUE,
            last_use TEXT);''')

    class Meta:
        database = db
