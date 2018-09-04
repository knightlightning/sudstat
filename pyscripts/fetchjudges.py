#!/usr/bin/python3

import cgi
import json
from passdb import *
from jsonhelpers import *
from conn import *

def application(environ, start_response):
    data = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ, keep_blank_values=True)
    court = data['court'].value
    court_type = data['type'].value
    
    session = get_session(passport)
    
    if court_type == 'mir':
        jobs = session.query(JobPlace.id).filter(JobPlace.name.like('_%в {}%'.format(court.split()[0][:-2]))).all()
    else:    
        jobs = session.query(JobPlace.id).filter(JobPlace.name.like('{}%'.format(court))).all()
    
    judges = sorted(session.query(Judge).filter(Judge.job_place_id.in_(jobs)).order_by(Judge.surname, Judge.name).all())
    json_output = '{{"judges":{}}}'.format(json.dumps([serialize(j) for j in judges], default=datetime_handler))
    
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [json_output.encode('utf_8')]
