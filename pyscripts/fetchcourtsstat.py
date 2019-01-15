#!/usr/bin/python3

'''
Created on 9 нояб. 2017 г.

@author: kmironov
'''

from json import dumps
from sudstatdb import *
from jsonhelpers import *
from conn import *

class MyStatData:
    def __init__(self, stat_type):
        self.stat_type = stat_type
        self.stat_data = []
        
def my_handler(x):
    if isinstance(x, MyStatData):
        return x.__dict__
    return enum_handler(x)

from flask import Flask
application = Flask(__name__)

@application.route("/wsgi-bin/fetchcourtsstat", methods=['GET'])
def app():
    session = get_session(sudstat)
    
    stat = session.query(StatData).join(StatData.stat_type).order_by(StatData.year.desc())
    
    res = {}
    for s in stat.all():
        if s.stat_type.type not in res:
            res[s.stat_type.type] = MyStatData(s.stat_type.type)
        res[s.stat_type.type].stat_data.append({'year':s.year,'mod':s.quarter,'data':s.data})
    
    json_output = dumps({'data':list(res.values())}, default=my_handler)
    return json_output

if __name__ == "__main__":
    application.run()