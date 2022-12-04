import os.path
from data_table import *

config = ConfigParser()
config.read('settings.ini')
folder = config['path']
files = []
path = folder['path'].replace('"', '')
try:
    cur.execute('''SELECT path FROM data ORDER BY path''')
    query = [i[0] for i in cur.fetchall()]
    print(path)
    print(query)
    if folder['path'] and os.path.exists(path):
        for i in os.listdir(path):
            if (i[-3:] == 'csv' or i[-3:] == 'xls' or i[
                                                      -4:] == 'xlsx') and f'{path}/{i}' not in query and f'{path}/{i}' != name:
                files.append(f'{path}/{i}')
    print(files)
except:
    if folder['path'] and os.path.exists(path):
        for i in os.listdir(path):
            if (i[-3:] == 'csv' or i[-3:] == 'xls' or i[
                                                      -4:] == 'xlsx') and f'{path}/{i}' != name:
                files.append(f'{path}/{i}')

