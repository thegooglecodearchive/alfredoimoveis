# coding:utf8
from datetime import datetime, date
today = date.today()

def month_between(d1, d2):
    d1 = datetime.strptime(d1.__str__(), "%Y-%m-%d")
    d2 = datetime.strptime(d2.__str__(), "%Y-%m-%d")
    return abs((d2.month - d1.month))

def days_between(d1, d2):
    d1 = datetime.strptime(d1.__str__(), "%Y-%m-%d")
    d2 = datetime.strptime(d2.__str__(), "%Y-%m-%d")
    return  (d2-d1).days
    #abs((d2.day - d1.day))    

def calcula_meses_atraso(d1,d2):    
    """
        Caso a o dia atual seja maior do que o dia do vencimento da parcela eu tenho que considerar
        o mês atual como vencido e com isso acrescentar 1 nos meses de atraso
    """
    meses = month_between(d1,d2)
    if d2.day > d1.day:
        meses += 1
    return meses