#!/usr/bin/python3

'''
Created on 7 нояб. 2017 г.

@author: kmironov
'''

import json
from sudstatdb import *
from jsonhelpers import *

session = get_session('mysql://passport-admin:Selkit2@localhost/sudstat?charset=utf8')

courts = session.query(Court).all()
res = []

for c in courts:
    if session.query(AdmCharge).filter(AdmCharge.court_id == c.id).count() > 0 or\
       session.query(CivCharge).filter(CivCharge.court_id == c.id).count() > 0 or\
       session.query(CrimCharge).filter(CrimCharge.court_id == c.id).count() > 0:
          res.append(c)

print("Content-type: text/html;charset=utf-8\n")
print('{{"courts":{}}}'.format(json.dumps([serialize(c) for c in res])))
