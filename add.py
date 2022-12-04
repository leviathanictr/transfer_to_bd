from csv_excel import *
from check_new import *

con = psycopg2.connect(dbname=dbfacts['dbname'], user=dbfacts['user'],
                       password=dbfacts['password'], host=dbfacts['host'])

cur = con.cursor()


def add():
    files.append(name)
    try:
        for j in range(len(datatable)):
            start_name = files[j][0]
            cur.execute('''SELECT id FROM data ORDER BY id''')
            cur_query = cur.fetchall()
            id = int(cur_query[-1][0])
            cur.execute(
                f"INSERT INTO DATA (id,path) VALUES ('{id + 1}', '{start_name}:{files[j][2:]}')")

            cur.execute(f'''CREATE TABLE "{id + 1}"
                                    (
                                    index BIGINT PRIMARY KEY,
                                    num BIGINT,
                                    mp2 TEXT,
                                    emb TEXT,
                                    pin DOUBLE PRECISION,
                                    e13 BIGINT);''')
            for i in range(0, len(datatable)):
                cur.execute(
                    f'''INSERT INTO "{id + 1}" (index, num, mp2, emb, pin, e13) VALUES ('{i}', '{datatable[j][i][0]}', '{datatable[j][i][1]}', '{datatable[j][i][2]}', '{datatable[j][i][3]}', '{datatable[j][i][4]}')
                                    ''')
            print('успешно')
    except:
        for j in range(len(datatable)):
            start_name = files[j][0]
            cur.execute(
                f"INSERT INTO DATA (id,path) VALUES ('{100000000+j}', '{start_name}:{files[j][2:]}')")
            cur.execute(f'''CREATE TABLE "{100000000 + j}"
                                            (
                                            index BIGINT PRIMARY KEY,
                                            num BIGINT,
                                            mp2 TEXT,
                                            emb TEXT,
                                            pin DOUBLE PRECISION,
                                            e13 BIGINT);''')
            for i in range(0, len(datatable[j])):
                cur.execute(
                    f'''INSERT INTO "{100000000 + j}" (index, num, mp2, emb, pin, e13) VALUES ('{i}', '{datatable[j][i][0]}', '{datatable[j][i][1]}', '{datatable[j][i][2]}', '{datatable[j][i][3]}', '{datatable[j][i][4]}')
                                    ''')
            print('безуспешно')