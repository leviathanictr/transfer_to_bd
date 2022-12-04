from configparser import ConfigParser
from csv_excel import *
import pandas as pd
from peewee import *

class Csv_table(Model):
    index = PrimaryKeyField()
    num = BigIntegerField()
    mp2 = TextField()
    emb = TextField()
    pin = DoubleField()
    e13 = BigIntegerField()

    class Meta:
        database = db



def csv_table_full():
    for i in range(0, len(datatable)):
        Csv_table(
            num=datatable[i][0],
            mp2=datatable[i][1],
            emb=str(datatable[i][2]),
            pin=datatable[i][3],
            e13=datatable[i][4]
        ).save()

