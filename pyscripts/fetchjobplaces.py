#!/usr/bin/python3

from json import dumps
from passdb import *
from jsonhelpers import *
from conn import *

from flask import Flask
application = Flask(__name__)

@application.route("/wsgi-bin/fetchjobplaces")
def app():
    session = get_session(passport)
    jobs = session.query(JobPlace).all()
    json_output = '{{"job_places":{}}}'.format(dumps([serialize(j) for j in jobs]))
    
    return json_output

if __name__ == "__main__":
    application.run()
