#!/usr/bin/python3

import cgi
import json
from passdb import *
from jsonhelpers import *
from conn import *

def application(environ, start_response):
    data = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ, keep_blank_values=True)
    judge_id = data['judge_id'].value
    
    session = get_session(passport)
    
    judge = session.query(Judge).filter(Judge.id == judge_id).one()
    
    json_output = '{{"judge":{},"degrees":{},"awards":{},"educations":{},"jobs":{}}}'.format(
    json.dumps(serialize(judge), default=datetime_handler),
    json.dumps([serialize(d) for d in judge.academic_degrees], default=datetime_handler) if judge.academic_degrees else '[]',
    json.dumps([serialize(a) for a in judge.awards], default=datetime_handler) if judge.awards else '[]',
    json.dumps([serialize(e) for e in judge.educations], default=datetime_handler) if judge.educations else '[]',
    json.dumps([serialize(j) for j in judge.jobs], default=datetime_handler) if judge.jobs else '[]')
    
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [json_output.encode('utf_8')]
    
