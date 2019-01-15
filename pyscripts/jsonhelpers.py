'''
Created on 4 окт. 2017 г.

@author: kmironov
'''

from datetime import date
from sqlalchemy.orm import class_mapper
import enum

def serialize(model):
    """Transforms a model into a dictionary which can be dumped to JSON."""
    columns = [c.key for c in class_mapper(model.__class__).columns]
    return dict((c, getattr(model, c)) for c in columns)
 
def datetime_handler(x):
    if isinstance(x, date):
        return x.isoformat()
    raise TypeError("Unknown type")

def enum_handler(x):
    if isinstance(x, enum.Enum):
        return str(x.value)
    raise TypeError("Unknown type")
