#!/usr/bin/python3

from json import dumps
from passdb import *
from jsonhelpers import *
from conn import *

from flask import Flask
application = Flask(__name__)

@application.route("/wsgi-bin/fetchjudgeinfo/<judge_id>", methods=['GET'])
def app(judge_id):
    session = get_session(passport)
    
    judge = session.query(Judge).filter(Judge.id == judge_id).one()
    
    json_output = '{{"judge":{},"degrees":{},"awards":{},"educations":{},"jobs":{}}}'.format(
    dumps(serialize(judge), default=datetime_handler),
    dumps([serialize(d) for d in judge.academic_degrees], default=datetime_handler) if judge.academic_degrees else '[]',
    dumps([serialize(a) for a in judge.awards], default=datetime_handler) if judge.awards else '[]',
    dumps([serialize(e) for e in judge.educations], default=datetime_handler) if judge.educations else '[]',
    dumps([serialize(j) for j in judge.jobs], default=datetime_handler) if judge.jobs else '[]')

    return json_output
    
if __name__ == "__main__":
    application.run()