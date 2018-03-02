#!/usr/bin/python3

import cgi
import json
from passdb import *
from jsonhelpers import *

data = cgi.FieldStorage()
judge_id = data['judge_id'].value

session = get_session('mysql://passport-admin:Selkit2@localhost/passport?charset=utf8')

judge = session.query(Judge).filter(Judge.id == judge_id).one()

json_output = '{{"judge":{},"degrees":{},"awards":{},"educations":{},"jobs":{}}}'.format(
json.dumps(serialize(judge), default=datetime_handler),
json.dumps([serialize(d) for d in judge.academic_degrees], default=datetime_handler) if judge.academic_degrees else '[]',
json.dumps([serialize(a) for a in judge.awards], default=datetime_handler) if judge.awards else '[]',
json.dumps([serialize(e) for e in judge.educations], default=datetime_handler) if judge.educations else '[]',
json.dumps([serialize(j) for j in judge.jobs], default=datetime_handler) if judge.jobs else '[]')

print("Content-type: text/html;charset=utf-8\n")
print(json_output)

