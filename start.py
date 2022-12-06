from configparser import ConfigParser

import psycopg2

from tkinter_choose import tkinter_choose

# Открываем конфиг
config = ConfigParser()

config.read('settings.ini')
dbfacts = config['database']
# Задаем базу данных
con = psycopg2.connect(dbname=dbfacts['dbname'], user=dbfacts['user'],
                       password=dbfacts['password'], host=dbfacts['host'])

cur = con.cursor()


# Вызываем tkinter_choose из другого файла, который выведет диалоговое окно для выбора пути, если он не в папке
name = tkinter_choose()
