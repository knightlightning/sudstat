#!/usr/bin/python3

'''
Created on 7 нояб. 2017 г.

@author: kmironov
'''

import json
from sudstatdb import *
from jsonhelpers import *
from conn import *

from flask import Flask
application = Flask(__name__)

@application.route("/wsgi-bin/fetchchargecourts", methods=['GET'])
def app():
    session = get_session(sudstat)
    
    courts = session.query(Court).all()
    res = []
    
    for c in courts:
        if session.query(AdmCharge).filter(AdmCharge.court_id == c.id).count() > 0 or\
           session.query(CivCharge).filter(CivCharge.court_id == c.id).count() > 0 or\
           session.query(CrimCharge).filter(CrimCharge.court_id == c.id).count() > 0:
              res.append(c)
    
    json_output = '{{"courts":{}}}'.format(json.dumps([serialize(c) for c in res]))
    
    return json_output

if __name__ == "__main__":
    application.run()
