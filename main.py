from add import *

cur.execute('COMMIT')
# создаем таблицу data
try:
    cur.execute('''CREATE TABLE DATA
            (
            id BIGINT PRIMARY KEY NOT NULL,
            path TEXT UNIQUE,
            last_use TEXT);''')
except:
    pass  # ЕСли она уже создана, просто пропускаем
cur.execute("COMMIT")
add()  # Вызываем функцию add()
