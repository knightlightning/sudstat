#!/usr/bin/python3

'''
Created on 20 окт. 2017 г.

@author: kmironov
'''

from json import dumps
import enum
from datetime import date
from sudstatdb import *
from sqlalchemy import and_
from conn import *

from flask import Flask
application = Flask(__name__)

@application.route("/wsgi-bin/fetchchargestat/<court_id>/<charge_type>", methods=['GET'])
def app(court_id, charge_type):
    session = get_session(sudstat)
    
    class ChargeClasses(enum.Enum):
        adm = (AdmCharge, AdmChargeData, AdmStatType)
        civ = (CivCharge, CivChargeData, CivStatType)
        crim = (CrimCharge, CrimChargeData, CrimStatType)
    
    class JudgeCharge:
        def __init__(self, name):
            self.name = name
            self.stat = []
    
    class Charge:
        def __init__(self, year, mod):
            self.year = year
            self.mod = mod
            self.data = []
        def append(self, judge, stat):
    #         if judge not in self.data:
    #             self.data[judge] = [stat]
    #         else:
    #             self.data[judge].append(stat)
            j = next((x for x in self.data if x.name == judge), None)
            if j == None:
                j = JudgeCharge(judge)
                self.data.append(j)
            j.stat.append(stat)
    
    def my_handler(x):
        if isinstance(x, date):
            return x.isoformat()
        if isinstance(x, Charge) or isinstance(x, JudgeCharge):
            return x.__dict__
        raise TypeError("Unknown type")
    
    
    cls = ChargeClasses[charge_type]
    charge_cls = cls.value[0]
    charge_data_cls = cls.value[1]
    charge_stat_cls = cls.value[2]
    charge = session.query(charge_cls.year,
                           charge_cls.modification,
                           charge_data_cls.data,
                           Judge.name)\
        .filter(and_(charge_cls.court_id == court_id))\
        .join(charge_cls.data)\
        .join(charge_data_cls.judge)\
        .join(charge_data_cls.stat_type)\
        .order_by(charge_cls.year.desc(),
                  Judge.name.asc(),
                  charge_stat_cls.col_number.asc())
    
    res = {}
    for c in charge.all():
        if c.year not in res:
            res[c.year] = Charge(c.year, c.modification)
        #print(c.year, c.modification, c.name.ljust(20), c.ext_id, c.description.ljust(30), c.data)
        res[c.year].append(c.name, c.data)
        
    stat_columns = [x.description for x in session.query(charge_stat_cls.description).order_by(charge_stat_cls.col_number).all()]
    data = sorted(list(res.values()), key=lambda x: x.year, reverse=True)
        
    json_output = '{}'.format(dumps({'stat_columns':stat_columns, 'data':data}, default=my_handler))
    
    return json_output

if __name__ == "__main__":
    application.run()
