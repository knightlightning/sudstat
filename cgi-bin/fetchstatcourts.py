#!/usr/bin/python3

'''
Created on 19 окт. 2017 г.

@author: kmironov
'''

import json
from sudstatdb import *
from jsonhelpers import *

session = get_session('mysql://passport-admin:Selkit2@localhost/sudstat?charset=utf8')

courts = session.query(Court).all()
    
json_output = '{{"courts":{}}}'.format(json.dumps([serialize(c) for c in courts]))

print("Content-type: text/html;charset=utf-8\n")
print(json_output)
        
