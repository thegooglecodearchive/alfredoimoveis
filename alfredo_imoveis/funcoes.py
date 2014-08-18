# coding:utf8
from datetime import *
from dateutil.relativedelta import *
import calendar

today = date.today()


def month_between(d1, d2):
    dif = 0
    d1 = datetime.strptime(d1.__str__(), "%Y-%m-%d")
    d2 = datetime.strptime(d2.__str__(), "%Y-%m-%d")

    if d2.year > d1.year:
        dif = (d2.year - d1.year) * 12

    dif += abs((d2.month - d1.month))
    return dif


def days_between(d1, d2):
    d1 = datetime.strptime(d1.__str__(), "%Y-%m-%d")
    d2 = datetime.strptime(d2.__str__(), "%Y-%m-%d")
    return (d2-d1).days
    #abs((d2.day - d1.day))


def calcula_meses_atraso(d1, d2):
    """
        Caso a o dia atual seja maior do que o
        dia do vencimento da parcela eu tenho que considerar
        o mês atual como vencido e com isso acrescentar 1 nos meses de atraso
    """
    meses = month_between(d1, d2)
    if d2.day > d1.day:
        meses += 1
    return meses


def incrementa_mes(data, qtd_meses):
    return data + relativedelta(months=+qtd_meses)


def incrementa_dias(data, qtd_dias):
    return data + relativedelta(days=+qtd_dias)
