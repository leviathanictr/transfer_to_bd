import pandas as pd

import csv


# Функция преоброзования файла в список данных
def is_csv_or_excel(name):
    if name[-3:] == 'xls' or name[-4:] == 'xlsx':
        return list(pd.read_excel(name).iloc)
    else:
        with open(name) as f:
            order = ['num', 'mp2', 'emb', 'pin', 'e13']
            return [[row['num'], row['mp2'], row['emb'], row['pin'], row['e13']] for row in
                    csv.DictReader(f, delimiter=',', fieldnames=order)][1:]
