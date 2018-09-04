#!/usr/bin/python3

import json
from passdb import *
from jsonhelpers import *
from conn import *

def application(environ, start_response):
    session = get_session(passport)
    jobs = session.query(JobPlace).all()
    json_output = '{{"job_places":{}}}'.format(json.dumps([serialize(j) for j in jobs]))
    
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [json_output.encode('utf_8')]
