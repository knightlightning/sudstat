#!/usr/bin/python3

import json
from passdb import *
from jsonhelpers import *

session = get_session('mysql://passport-admin:Selkit2@localhost/passport?charset=utf8')
jobs = session.query(JobPlace).all()
json_output = '{{"job_places":{}}}'.format(json.dumps([serialize(j) for j in jobs]))

print("Content-type: text/html;charset=utf-8\n")
print(json_output)

