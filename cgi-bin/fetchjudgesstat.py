#!/usr/bin/python3

'''
Created on 20 окт. 2017 г.

@author: kmironov
'''

import json
from sudstatdb import *
from jsonhelpers import *

session = get_session('mysql://passport-admin:Selkit2@linux-test.omsksud.ru/sudstat?charset=utf8')

class PeriodData:
    def __init__(self, year):
        self.year = year
        self.data = [None] * 4

class CourtData:
    def __init__(self, court, years):
        self.court = court
        self.data = [PeriodData(y) for y in years]

    def append(self, y, q, d):
        self.data[next(i for i, x in enumerate(self.data) if x.year == y)].data[q] = d
    
def my_handler(x):
    if isinstance(x, PeriodData) or isinstance(x, CourtData):
        return x.__dict__
    raise TypeError("Unknown type")

charges = session.query(RaiCharge).all()
periods = session.query(Period).filter(Period.id.in_([c.period_id for c in charges])).order_by(Period.year.desc(), Period.quarter.asc()).all()

years = sorted({p.year: None for p in periods}.keys(), reverse=True)
courts_data = {c.id: CourtData(c.name, years) for c in session.query(Court).all()}

for p in periods:
    for ch in filter(lambda x: x.period_id == p.id, charges):
        courts_data[ch.court_id].append(p.year, p.quarter.value, ch.data)

json_output = '{{"courts":{}}}'.format(json.dumps(list(courts_data.values()), default=my_handler))
print("Content-type: text/html;charset=utf-8\n")
print(json_output)
