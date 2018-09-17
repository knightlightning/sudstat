#!/usr/bin/python3
'''
Created on 16 нояб. 2017 г.

@author: kmironov
'''

import cgi
from os.path import splitext
from os import remove
import uuid
from sqlalchemy import and_
import sys
sys.path.append('/usr/share/sudstat')
from pyscripts.sudstatdb import *
from pyscripts.conn import *

from flask import Flask
from flask import request
application = Flask(__name__)

@application.route("/wsgi-bin/uploadstatfile", methods=['POST'])
def app(): 
    file_path = '/usr/share/sudstat/resource/pdf'
    
    data = request.form
    stat_type = data['stat_type']
    year = data['year']
    quarter = data['quarter']
    myfile = request.files['file']

    session = get_session(sudstat)

    file_ext = splitext(myfile.filename)[-1]
    file_name = '{}{}'.format(uuid.uuid4().hex, file_ext)
    myfile.save('{}/{}'.format(file_path, file_name))

    stat_type_id = session.query(StatType).filter(StatType.type == stat_type).one().id
    stat = session.query(StatData).filter(and_(StatData.year == year, StatData.stat_type_id == stat_type_id)).first()
    if stat == None:
        stat = StatData(stat_type_id = stat_type_id, year = year, quarter = quarter, data = file_name)
        session.add(stat)
    else:
        try:
            remove('{}/{}'.format(file_path, stat.data))
        except OSError:
            pass
        stat.quarter = quarter
        stat.data = file_name
    
    session.commit()
    
    return "OK"

if __name__ == "__main__":
    application.run()
