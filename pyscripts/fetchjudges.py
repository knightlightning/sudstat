#!/usr/bin/python3

from json import dumps
from passdb import *
from jsonhelpers import *
from conn import *

from flask import Flask
application = Flask(__name__)

@application.route("/wsgi-bin/fetchjudges/<path:court>/<court_type>", methods=['GET'])
def app(court, court_type):
    session = get_session(passport)
    
    if court_type == 'mir':
        jobs = session.query(JobPlace.id).filter(JobPlace.name.like('_%в {}%'.format(court.split()[0][:-2]))).all()
    else:    
        jobs = session.query(JobPlace.id).filter(JobPlace.name.like('{}%'.format(court))).all()
    
    judges = sorted(session.query(Judge).filter(Judge.job_place_id.in_(jobs)).order_by(Judge.surname, Judge.name).all())
    json_output = '{{"judges":{}}}'.format(dumps([serialize(j) for j in judges], default=datetime_handler))

    return json_output

if __name__ == "__main__":
    application.run()