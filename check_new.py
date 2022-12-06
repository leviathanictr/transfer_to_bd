import os.path

from start import *

# Открываем конфиг
config = ConfigParser()
config.read('settings.ini')
folder = config['path']
files = []  # Список файлов
path = folder['path'].replace('"', '')  # Путь папки с файлами
try:
    cur.execute('''SELECT path FROM data ORDER BY path''')
    query = [i[0] for i in cur.fetchall()]  # Находим все пути в data, если таковые существуют
    if name in query:  # Если выбранный файл находится в data, сделать из него пустую строку
        name = ''
    if folder['path'] and os.path.exists(path):
        for i in os.listdir(path):  # При существовании папки и файлов в ней добавляем все файлы,
            # которые не являются временными и подходят по типу данных,
            # а также не совпадают с выбранным намит заранее файлов, в переменную files
            if (i[-3:] == 'csv' or i[-3:] == 'xls' or i[
                                                      -4:] == 'xlsx') and f'{path}/{i}' not in query and f'{path}/{i}' \
                    != name and i[
                                :2] != '~$':
                files.append(f'{path}/{i}')

# Все то же самое, но не проверяем на наличие в таблице, т.к. ее еще нет
except:
    if folder['path'] and os.path.exists(path):
        for i in os.listdir(path):
            if (i[-3:] == 'csv' or i[-3:] == 'xls' or i[
                                                      -4:] == 'xlsx') and f'{path}/{i}' != name and i[:2] != '~$':
                files.append(f'{path}/{i}')
