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

file_path = '/usr/share/sudstat/resource/pdf'

data = cgi.FieldStorage()
stat_type = data['stat_type'].value
year = data['year'].value
quarter = data['quarter'].value
myfile = data['file']

session = get_session('mysql://passport-admin:Selkit2@localhost/sudstat?charset=utf8')

print("Content-type: text/html;charset=utf-8\n")

file_ext = splitext(myfile.filename)[-1]
file_name = '{}{}'.format(uuid.uuid4().hex, file_ext)
with open('{}/{}'.format(file_path, file_name), 'wb') as f:
    f.write(myfile.file.read())

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
