'''
Created on 3 окт. 2017 г.

@author: kmironov
'''

from sqlalchemy import Column, ForeignKey, Integer, Text, Date, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
 
class JobPlace(Base):
    __tablename__ = 'job_places'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)

class AcademicDegree(Base):
    __tablename__ = 'academic_degrees'
    id = Column(Integer, primary_key=True)
    judge_id = Column(Integer, ForeignKey('judges.id'))
    name = Column(Text, nullable=False)
    order_text = Column(Text, nullable=False)
    order_date = Column(Date, nullable=False)
    
class Award(Base):
    __tablename__ = 'awards'
    id = Column(Integer, primary_key=True)
    judge_id = Column(Integer, ForeignKey('judges.id'))
    name = Column(Text, nullable=False)
    certificate_type = Column(Text, nullable=True)
    certificate_number = Column(Text, nullable=False)
    certificate_date = Column(Date, nullable=False)
    
class Education(Base):
    __tablename__ = 'educations'
    id = Column(Integer, primary_key=True)
    judge_id = Column(Integer, ForeignKey('judges.id'))
    school = Column(Text, nullable=False)
    type = Column(Text, nullable=True)
    graduation_date = Column(Date, nullable=False)
    specialization = Column(Text, nullable=True)
    qualification = Column(Text, nullable=True)

class JobHistory(Base):
    __tablename__ = 'job_history'
    id = Column(Integer, primary_key=True)
    judge_id = Column(Integer, ForeignKey('judges.id'))
    place = Column(Text, nullable=False)
    position = Column(Text, nullable=True)
    acceptance_date = Column(Date, nullable=False)
    discharge_date = Column(Date, nullable=True)
    city = Column(Text, nullable=True)

class Judge(Base):
    __tablename__ = 'judges'
    id = Column(Integer, primary_key=True)
    surname = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    patron = Column(Text, nullable=False)
    citizenship = Column(Text, nullable=True)
    birthplace = Column(Text, nullable=False)
    birthdate = Column(Date, nullable=False)
    job_place_id = Column(Integer, ForeignKey('job_places.id'))
    #job_place = relationship(JobPlace)
    job_position = Column(Text, nullable=False)
    job_acceptance_day = Column(Date, nullable=False)
    qualifier_class_name = Column(Text, nullable=True)
    qualifier_class_reason = Column(Text, nullable=True)
    qualifier_class_date = Column(Date, nullable=True)
    assignment_order = Column(Text, nullable=False)
    assignment_date = Column(Date, nullable=False)
    previous_judge_exp_years = Column(Integer, nullable=False)
    previous_judge_exp_months = Column(Integer, nullable=False)
    previous_judge_exp_days = Column(Integer, nullable=False)
    previous_law_exp_years = Column(Integer, nullable=False)
    previous_law_exp_months = Column(Integer, nullable=False)
    previous_law_exp_days = Column(Integer, nullable=False)
    avatar = Column(VARCHAR(length=64), nullable=True)
    upload_date = Column(Date, nullable=False)
    def __lt__(self, r):
        if 'председатель суда' in self.job_position.lower() or 'председатель' == self.job_position.lower():
            return True
        if 'заместитель' in self.job_position.lower():
            if 'заместитель' in r.job_position.lower():
                return self.surname < r.surname
            if 'председатель суда' in r.job_position.lower() or 'председатель' == r.job_position.lower():
                return False;
            else:
                return True;
        return False
    academic_degrees = relationship(AcademicDegree, lazy='select')
    awards = relationship(Award, lazy='select')
    educations = relationship(Education, lazy='select')
    jobs = relationship(JobHistory, lazy='select')

def get_session(conn):
    engine = create_engine(conn)
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()
    session.autoflush = True
    return session
