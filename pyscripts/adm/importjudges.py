#!/usr/bin/python3

'''
Created on 3 окт. 2017 г.

@author: kmironov
'''

import os
import sys
from sqlalchemy import and_
import judgefromxml
import traceback
sys.path.append('/usr/share/sudstat')
from pyscripts.passdb import *
from sse import *

def get_job_place(name):
    j = session.query(JobPlace).filter(JobPlace.name == name).first()
    if j:
        return j
    else:
        j = JobPlace(name = name)
        session.add(j)
        session.commit()
        return j
    
def delete_judge(_id):
    session.query(Award).filter_by(judge_id=_id).delete()
    session.query(Education).filter_by(judge_id=_id).delete()
    session.query(AcademicDegree).filter_by(judge_id=_id).delete()
    session.query(JobHistory).filter_by(judge_id=_id).delete()
    #session.query(Judge).filter_by(id=_id).delete()
    j = session.query(Judge).filter_by(id=_id)
    avatar = j.one().avatar
    if avatar:
        try:
            os.remove('{}/{}'.format(avatar_path, avatar))
        except OSError:
            pass
    j.delete()

session = get_session('mysql://passport-admin:Selkit2@localhost/passport?charset=utf8')
avatar_path = '/usr/share/sudstat/resource/img'
mypath = {'obl': b'/srv/judges-xml/obl', 'rai': b'/srv/judges-xml/rai'}
upload_date = datetime.now().date()
args = sys.argv[1].split(':')
delete_input_files = (args[2] == 'delete')

files = []
for arg in args:
    if arg in mypath:
        for root, dirs, ff in os.walk(mypath[arg]):
            for f in ff:
                files.append(os.path.join(root, f).decode('utf-8'))

print('Content-Type: text/event-stream\n')
print('Cache-Control: no-cache\n')

#files = [files[-1]]
for f in files:
    # Deal with XML file. Error possibility is high.
    try:
        print_sse(SSEType.info, 'Processing file "{}"...'.format(f))
        judge_xml = judgefromxml.JudgeFromXml(f)
        
        law_exp = judge_xml.get_law_exp()
        judge_exp = judge_xml.get_judge_exp()
        qc = judge_xml.get_qualifier_class()
        assign = judge_xml.get_prev_assignment()
        job_place = get_job_place(judge_xml.get_job_name())
                
        judge_db = Judge(
            surname = judge_xml.get_surname(),
            name = judge_xml.get_name(),
            patron = judge_xml.get_patron(),
            birthplace = judge_xml.get_birthplace(),
            birthdate = judge_xml.get_birthdate(),
            citizenship = judge_xml.get_citizenship(),
            job_place_id = job_place.id,
            job_position = judge_xml.get_job_position(),
            job_acceptance_day = judge_xml.get_job_acceptance_date(),
            qualifier_class_name = qc.name,
            qualifier_class_reason = qc.reason,
            qualifier_class_date = qc.date,
            assignment_order = assign.reason,
            assignment_date = assign.date,
            previous_judge_exp_years = judge_exp.y,
            previous_judge_exp_months = judge_exp.m,
            previous_judge_exp_days = judge_exp.d,
            previous_law_exp_years = law_exp.y,
            previous_law_exp_months = law_exp.m,
            previous_law_exp_days = law_exp.d,
            avatar = judge_xml.write_avatar(avatar_path),
            upload_date = upload_date)

        degrees = judge_xml.get_degrees()
        awards = judge_xml.get_awards()
        educations = judge_xml.get_educations()
        job_history = judge_xml.get_job_history()
            
    except Exception as e:
        print_sse(SSEType.error, '{} cannot be imported. Invalid XML-schema format {}.'.format(judge_xml.get_surname(), traceback.format_exc()))
        continue
    
    # Deal with DB. Error possibility is not that high.
    try:
        for j in session.query(Judge).filter(and_(Judge.surname == judge_db.surname,
                                                  Judge.name == judge_db.name,
                                                  Judge.patron == judge_db.patron,
                                                  Judge.job_place_id == job_place.id)).all():
            print_sse(SSEType.warning, 'Judge {} ({}) already exists. Deleting...'.format(judge_db.surname, j.id))
            delete_judge(j.id)

        session.add(judge_db)
        session.commit() # we have to know judge ID.
        
        for d in degrees:
            session.add(AcademicDegree(judge_id = judge_db.id, name = d.name, order_text = d.order_text, order_date = d.order_date))
            
        for a in awards:
            session.add(Award(judge_id = judge_db.id, name = a.name, certificate_type = a.certificate_type, certificate_number = a.certificate_number, certificate_date = a.certificate_date))
            
        for e in educations:
            session.add(Education(judge_id = judge_db.id, school = e.school, type = e.type, graduation_date = e.graduation_date, specialization = e.specialization, qualification = e.qualification))
            
        for h in job_history:
            session.add(JobHistory(judge_id = judge_db.id, place = h.place, position = h.position, acceptance_date = h.acceptance_date, discharge_date = h.discharge_date, city = h.city))
              
        print_sse(SSEType.info, '{} has been imported successfuly.'.format(judge_db.surname))

        session.commit()
        
    except Exception as e:
        print_sse(SSEType.error, '{} cannot be imported: {}.'.format(judge_db.surname, e))
        session.rollback()
        raise
    
    if delete_input_files:
        print_sse(SSEType.info, 'Deleting file "{}"...'.format(f))
        try:
            os.remove(f.encode('utf-8'))
        except OSError as e:
            print_sse(SSEType.error, '{} cannot be deleted: {}.'.format(f, e))

print_sse(SSEType.info, 'Deleting outdated records...')
try:
    oblsud_id = get_job_place('Омский областной суд').id
    for arg in [a for a in args if a in ['obl','rai']]:
        for j in session.query(Judge).filter(and_(Judge.upload_date < upload_date,
              Judge.job_place_id == oblsud_id if arg == 'obl' else Judge.job_place_id != oblsud_id)).all():
            print_sse(SSEType.info, 'Judge {} ({}) is outdated. Deleting...'.format(j.surname, j.id))
            delete_judge(j.id)
    session.commit()
except Exception as e:
    print_sse(SSEType.error, 'Error occured during deletion process: {}. Rolling back...'.format(e))
    session.rollback()

print_sse(SSEType.info, 'Everything is done.')
print_sse(SSEType.system, 'END-OF-STREAM')
