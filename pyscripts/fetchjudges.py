#!/usr/bin/python3

import cgi
import json
from passdb import *
from jsonhelpers import *
from conn import *

data = cgi.FieldStorage()
court = data['court'].value
court_type = data['type'].value

session = get_session(passport)

if court_type == 'mir':
    jobs = session.query(JobPlace.id).filter(JobPlace.name.like('_%в {}%'.format(court.split()[0][:-2]))).all()
else:    
    jobs = session.query(JobPlace.id).filter(JobPlace.name.like('{}%'.format(court))).all()

judges = sorted(session.query(Judge).filter(Judge.job_place_id.in_(jobs)).order_by(Judge.surname, Judge.name).all())
json_output = '{{"judges":{}}}'.format(json.dumps([serialize(j) for j in judges], default=datetime_handler))

print("Content-type: text/html;charset=utf-8\n")
print(json_output)

