from check_new import *
from csv_excel import *


def add():
    files.append(name)  # Добавляем к переменной files первый выбранный нами файл
    if files == ['']:  # Если файлов нет, заканчиваем работу
        quit()
    elif name == '':  # Если мы не выбирали файл, то пустая строка убирается из files
        files.remove(name)
    # Если таблица data уже имеет "rows", то есть строки, заходим в try
    try:
        for names in files:  # Проходим по каждому файлу
            start_name = names[0]
            cur.execute('''SELECT id FROM data ORDER BY id''')
            cur_query = cur.fetchall()
            id = int(cur_query[-1][0])  # Находим последний id в таблице, чтобы создать следующий
            cur.execute(
                f"INSERT INTO DATA (id,path) VALUES ('{id + 1}', '{start_name}:{names[2:]}')")
            # Создаем еще один "row" в таблице data

            # Создаем таблицу с названием в виде предыдущего id, но на 1 больше
            cur.execute(f'''CREATE TABLE "{id + 1}"
                                    (
                                    index BIGINT PRIMARY KEY,
                                    num BIGINT,
                                    mp2 TEXT,
                                    emb TEXT,
                                    pin DOUBLE PRECISION,
                                    e13 BIGINT);''')
            datatable = is_csv_or_excel(names)  # Вызываем is_csv_or_excel()
            for i in range(0, len(datatable)):
                cur.execute(
                    f'''INSERT INTO "{id + 1}" (index, num, mp2, emb, pin, e13) VALUES ('{i}', '{datatable[i][0]}', 
                    '{datatable[i][1]}', '{datatable[i][2]}', '{datatable[i][3]}', '{datatable[i][4]}')
                                    ''')  # Заполняем только что созданную таблицу данным из файла
            id += 1
    except:
        for j in range(len(files)):
            start_name = files[j][0]
            cur.execute(
                f"INSERT INTO DATA (id,path) VALUES ('{100000000 + j}', '{start_name}:{files[j][2:]}')")
            cur.execute(f'''CREATE TABLE "{100000000 + j}"
                                            (
                                            index BIGINT PRIMARY KEY,
                                            num BIGINT,
                                            mp2 TEXT,
                                            emb TEXT,
                                            pin DOUBLE PRECISION,
                                            e13 BIGINT);''')
            datatable = is_csv_or_excel(files[j])
            for i in range(0, len(datatable[j])):
                cur.execute(
                    f'''INSERT INTO "{100000000 + j}" (index, num, mp2, emb, pin, e13) VALUES ('{i}', 
                    '{datatable[i][0]}', '{datatable[i][1]}', '{datatable[i][2]}', '{datatable[i][3]}', '{datatable[i][4]}')
                                    ''')
                # Все то же самое, но id задается с 1000000 и увеличивается на 1 для каждого следующего элемента
                # Актуально только при пустой data
