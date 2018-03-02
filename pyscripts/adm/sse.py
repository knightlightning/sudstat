#!/usr/bin/python3

'''
Created on Feb 28, 2018

@author: kmironov
'''

import enum
import json
from datetime import datetime

class SSEType(enum.Enum):
    info = 1
    error = 2
    system = 3

def print_sse(type, msg):
    data = {'type': type.name, 'message': msg, 'timestamp': str(datetime.now())}
    print('data: {}\n'.format(json.dumps(data)), flush=True)
