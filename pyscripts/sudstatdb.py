'''
Created on 18 окт. 2017 г.

@author: kmironov
'''

from sqlalchemy import Column, ForeignKey, Integer, VARCHAR, TEXT, Date, ForeignKeyConstraint, PrimaryKeyConstraint, Enum
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import enum

class Quarter(enum.Enum):
    first = 'I'
    second = 'II'
    third = 'III'
    fourth = 'IV'

Base = declarative_base()

class Court(Base):
    __tablename__ = 'courts'
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(length=128), nullable=False)

class Judge(Base):
    __tablename__ = 'judges'
    court_id = Column(Integer, ForeignKey('courts.id'), primary_key=True)
    ext_id = Column(Integer, primary_key=True)
    name = Column(TEXT, nullable=False)
    __table_args__ = (
         PrimaryKeyConstraint('court_id', 'ext_id'),
     )
    #data = relationship('AdmChargeData', back_populates='judge', lazy='select')

class AdmStatType(Base):
    __tablename__ = 'adm_stat_types'
    id = Column(Integer, primary_key=True)
    col_number = Column(Integer, nullable=False)
    description = Column(TEXT, nullable=False)

class CivStatType(Base):
    __tablename__ = 'civ_stat_types'
    id = Column(Integer, primary_key=True)
    col_number = Column(Integer, nullable=False)
    description = Column(TEXT, nullable=False)

class CrimStatType(Base):
    __tablename__ = 'crim_stat_types'
    id = Column(Integer, primary_key=True)
    col_number = Column(Integer, nullable=False)
    description = Column(TEXT, nullable=False)

class AdmCharge(Base):
    __tablename__ = 'adm_charge'
    year = Column(Integer, primary_key=True)
    court_id = Column(Integer, ForeignKey('courts.id'), primary_key=True)
    modification = Column(Date, nullable=False)
    __table_args__ = (
         PrimaryKeyConstraint('year', 'court_id'),
     )
    data = relationship('AdmChargeData', back_populates='charge', lazy="dynamic")

class CivCharge(Base):
    __tablename__ = 'civ_charge'
    year = Column(Integer, primary_key=True)
    court_id = Column(Integer, ForeignKey('courts.id'), primary_key=True)
    modification = Column(Date, nullable=False)
    __table_args__ = (
         PrimaryKeyConstraint('year', 'court_id'),
     )
    data = relationship('CivChargeData', back_populates='charge', lazy="dynamic")

class CrimCharge(Base):
    __tablename__ = 'crim_charge'
    year = Column(Integer, primary_key=True)
    court_id = Column(Integer, ForeignKey('courts.id'), primary_key=True)
    modification = Column(Date, nullable=False)
    __table_args__ = (
         PrimaryKeyConstraint('year', 'court_id'),
     )
    data = relationship('CrimChargeData', back_populates='charge', lazy="dynamic")

class AdmChargeData(Base):
    __tablename__ = 'adm_charge_data'
    charge_court_id = Column(Integer, primary_key=True)
    charge_year = Column(Integer, primary_key=True)
    judge_court_id = Column(Integer, nullable=False)
    judge_ext_id = Column(Integer, primary_key=True)
    stat_type_id = Column(Integer, ForeignKey('adm_stat_types.id'), primary_key=True)
    __table_args__ = (
         PrimaryKeyConstraint('charge_court_id', 'charge_year', 'judge_ext_id', 'stat_type_id'),
         ForeignKeyConstraint(['charge_court_id', 'charge_year'], ['adm_charge.court_id', 'adm_charge.year']),
         ForeignKeyConstraint(['judge_court_id', 'judge_ext_id'], ['judges.court_id', 'judges.ext_id']),
    )    
    data = Column(Integer, nullable=True)
    charge = relationship('AdmCharge', back_populates='data')
    judge = relationship('Judge')
    stat_type = relationship('AdmStatType')
    
class CivChargeData(Base):
    __tablename__ = 'civ_charge_data'
    charge_court_id = Column(Integer, primary_key=True)
    charge_year = Column(Integer, primary_key=True)
    judge_court_id = Column(Integer, nullable=False)
    judge_ext_id = Column(Integer, primary_key=True)
    stat_type_id = Column(Integer, ForeignKey('civ_stat_types.id'), primary_key=True)
    __table_args__ = (
         PrimaryKeyConstraint('charge_court_id', 'charge_year', 'judge_ext_id', 'stat_type_id'),
         ForeignKeyConstraint(['charge_court_id', 'charge_year'], ['civ_charge.court_id', 'civ_charge.year']),
         ForeignKeyConstraint(['judge_court_id', 'judge_ext_id'], ['judges.court_id', 'judges.ext_id']),
    )    
    data = Column(Integer, nullable=True)
    charge = relationship('CivCharge', back_populates='data')
    judge = relationship('Judge')
    stat_type = relationship('CivStatType')
    
class CrimChargeData(Base):
    __tablename__ = 'crim_charge_data'
    charge_court_id = Column(Integer, primary_key=True)
    charge_year = Column(Integer, primary_key=True)
    judge_court_id = Column(Integer, nullable=False)
    judge_ext_id = Column(Integer, primary_key=True)
    stat_type_id = Column(Integer, ForeignKey('crim_stat_types.id'), primary_key=True)
    __table_args__ = (
         PrimaryKeyConstraint('charge_court_id', 'charge_year', 'judge_ext_id', 'stat_type_id'),
         ForeignKeyConstraint(['charge_court_id', 'charge_year'], ['crim_charge.court_id', 'crim_charge.year']),
         ForeignKeyConstraint(['judge_court_id', 'judge_ext_id'], ['judges.court_id', 'judges.ext_id']),
    )    
    data = Column(Integer, nullable=True)
    charge = relationship('CrimCharge', back_populates='data')
    judge = relationship('Judge')
    stat_type = relationship('CrimStatType')

# class Period(Base):
#     __tablename__ = 'periods'
#     id = Column(Integer, primary_key=True)
#     year = Column(Integer, nullable=False)
#     quarter = Column('quarter', Enum(Quarter), nullable=False)
 
class StatType(Base):
    __tablename__ = 'stat_types'
    id = Column(Integer, primary_key=True)
    type = Column(VARCHAR(length=128), nullable=False)
 
class StatData(Base):
    __tablename__ = 'stat_data'
    stat_type_id = Column(Integer, ForeignKey('stat_types.id'), primary_key=True)
    year = Column(Integer, primary_key=True)
    quarter = Column('quarter', Enum(Quarter), nullable=False)
    data = Column(VARCHAR(length=64), nullable=False)
    __table_args__ = (
        PrimaryKeyConstraint('stat_type_id', 'year'),
    )
    stat_type = relationship(StatType)

def get_session(conn):
    engine = create_engine(conn)
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()
    session.autoflush = True
    return session
