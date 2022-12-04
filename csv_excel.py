import csv
import pandas as pd
from check_new import *

datatable = []
if not files and not name:
    quit()
elif name[-3:] == 'xls' or name[-4:] == 'xlsx':
    files.append(name)
    for i in files:
        datatable.append(list(pd.read_excel(i).iloc))
else:
    files.append(name)
    for i in files:
        with open(name) as f:
            order = ['num', 'mp2', 'emb', 'pin', 'e13']
            datatable.append([[row['num'], row['mp2'], row['emb'], row['pin'], row['e13']] for row in csv.DictReader(f, fieldnames=order)][1:])