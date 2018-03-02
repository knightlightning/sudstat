import lxml.etree
#import re
from datetime import datetime
from functools import partial
from os.path import splitext
import base64
import uuid

def getelement(e, tree): return tree.xpath(e)
def getelementtext(e, tree): return getelement('{}/text()'.format(e), tree)[0]
    #res = getelement('{}/text()'.format(e), tree)
    #return res[0] if res else ""
def element2date(datetag, e): return datetime.strptime(getelementtext(datetag, e), '%d.%m.%Y').date()
def element2int(inttag, e): return int(getelementtext(inttag, e))

class Degree:
    def __init__(self, name, order_text, order_date):
        self.name = name
        self.order_text = order_text
        self.order_date = order_date
        
class Award:
    def __init__(self, name, certificate_type, certificate_number, certificate_date):
        self.name = name
        self.certificate_type = certificate_type
        self.certificate_number = certificate_number
        self.certificate_date = certificate_date
        
class Education:
    def __init__(self, school, _type, graduation_date, specialization, qualification):
        self.school = school
        self.type = _type
        self.graduation_date = graduation_date
        self.specialization = specialization
        self.qualification = qualification

class Job:
    def __init__(self, place, city, position, acceptance_date, discharge_date):
        self.place = place
        self.city = city
        self.position = position
        self.acceptance_date = acceptance_date
        self.discharge_date = discharge_date

class QC:
    def __init__(self, name, date, reason):
        self.name = name
        self.date = date
        self.reason = reason
        
class Assignment:
    def __init__(self, date, reason):
        self.date = date
        self.reason = reason
        
class Exp:
    def __init__(self, y, m, d):
        self.y = int(y)
        self.m = int(m)
        self.d = int(d)

class JudgeFromXml:
    def getelementbyid(self, id, idpath, elementname='.'):
        return [e.getparent().xpath('{}'.format(elementname))[0] for e in self.tree.xpath('{}[text()="{}"]'.format(idpath, id))]
    def getelementtextbyid(self, id, idpath, elementname='.'):
        return self.getelementbyid(id, idpath, '{}/text()'.format(elementname))
    def getelement(self, e):
        return self.tree.xpath(e)
    def getelementtext(self, e):
        return getelement('{}/text()'.format(e), self.tree)[0]
    
    def __init__(self, file):
#         with open(file, mode='r', errors='ignore') as f:
#             f.readline() # skip <?xml... line
#             data = f.read()
#         data = re.sub('(?:<CADRE_FILE_CONTENTS>((?:.*?\r?\n?)*)<\/CADRE_FILE_CONTENTS>)+', '', data).replace('&amp;quot;','&quot;')
#         self.tree = lxml.etree.fromstring(data)
        self.tree = lxml.etree.parse(file)
        
        self.person = self.getelement('/CARD/CADRE_PERSON')[0]
        self.judgeid = getelementtext('./ISN_PERSON120', self.person)
        for fio in self.getelementbyid(self.judgeid, '/CARD/CADRE_FIO/ISN_PERSON55'):
            if getelementtext('./ISACTIVE', fio) == '1':
                self.fio = fio
        self.job = self.getelementbyid(self.judgeid, '/CARD/CADRE_WORK/ISN_PERSON174')[0]

    def get_surname(self):
        return getelementtext('./SURNAME', self.fio)
    def get_name(self):
        return getelementtext('./NAME55', self.fio)
    def get_patron(self):
        return getelementtext('./PATRON', self.fio)
    def get_birthdate(self):
        return element2date('./BIRTHDAY', self.person)
    def get_birthplace(self):
        return getelementtext('./BIRTHPLACE', self.person)
    def get_citizenship(self):
        return self.getelementtextbyid(id = getelementtext('./ISN_CITIZENSHIP_CL', self.person),
                                       idpath = '/CARD/CADRE_CITIZENSHIP_CL/ISN_NODE17',
                                       elementname = 'CLASSIF_NAME17')[0] if getelement('./ISN_CITIZENSHIP_CL', self.person) else None
    
    def get_job_name(self):
        return self.getelementtextbyid(id = getelementtext('./ISN_ORGANIZATION_CL', self.person),
                                        idpath = '/CARD/CADRE_ORGANIZATION_CL/ISN_NODE114',
                                        elementname = 'CLASSIF_NAME114')[0]
    def get_job_acceptance_date(self):
        return element2date('ACCEPTANCE_DATE', self.job)
    
    def get_job_position(self):
        for w in sorted(self.tree.xpath('/CARD/CADRE_DISPLACEMENT[ISN_WORK42="{}"][ISN_PERSON42="{}"]'.format(getelementtext('./ISN_WORK174', self.job), self.judgeid)),
                key=partial(element2date, 'ASSIGNMENT_START_DATE'),
                reverse=True):
            return self.getelementtextbyid(getelementtext('ISN_STAFF', w), '/CARD/CADRE_STAFF/ISN_NODE154', 'OFFICE_SHORT')[0]
    
    def get_judge_exp(self):
        _id = self.getelementtextbyid(id = 'стаж работы в должности судьи',
                                      idpath = '/CARD/CADRE_KINDSENIORITY_CL/CLASSIF_NAME70',
                                      elementname = 'ISN_NODE70')
        if not _id:
            _id = self.getelementtextbyid(id = 'стаж работы в качестве судьи',
                                          idpath = '/CARD/CADRE_KINDSENIORITY_CL/CLASSIF_NAME70',
                                          elementname = 'ISN_NODE70')
        exp = self.tree.xpath('/CARD/CADRE_AMOUNTSENIORITY[ISN_KINDSENIORITY_CL="{}"][ISN_PERSON8="{}"]'.format(_id[0], self.judgeid))
        return Exp(getelementtext('./AMOUNTYEAR', exp[0]), getelementtext('./AMOUNTMONTH', exp[0]), getelementtext('./AMOUNTDAY', exp[0])) if exp else Exp(0, 0, 0)

    def get_law_exp(self):
        _id = self.getelementtextbyid(id = 'стаж работы в области юриспруденции',
                                      idpath = '/CARD/CADRE_KINDSENIORITY_CL/CLASSIF_NAME70',
                                      elementname = 'ISN_NODE70')[0]
        exp = self.tree.xpath('/CARD/CADRE_AMOUNTSENIORITY[ISN_KINDSENIORITY_CL="{}"][ISN_PERSON8="{}"]'.format(_id, self.judgeid))
        return Exp(getelementtext('./AMOUNTYEAR', exp[0]), getelementtext('./AMOUNTMONTH', exp[0]), getelementtext('./AMOUNTDAY', exp[0])) if exp else Exp(0, 0, 0)

    def get_degrees(self):
        return [Degree(getelementtext('./CLASSIF_NAME3', self.getelementbyid(getelementtext('./ISN_ACADEMICDEGREE_CL', d), '/CARD/CADRE_ACADEMICDEGREE_CL/ISN_NODE3')[0]),
                       getelementtext('ORDER_WHOM', d) if getelement('ORDER_WHOM', d) else None,
                       element2date('ORDER_DATE', d))
                 for d in sorted(self.getelementbyid(self.judgeid, '/CARD/CADRE_ACADEMICDEGREE/ISN_PERSON2'), key=partial(element2date, 'ORDER_DATE'))]

    def get_awards(self):
        return [Award(getelementtext('./CLASSIF_NAME58', self.getelementbyid(getelementtext('./ISN_GOVERNMENTAWARD_CL', a), '/CARD/CADRE_GOVERNMENTAWARD_CL/ISN_NODE58')[0]),
                      getelementtext('./CLASSIF_NAME16', self.getelementbyid(getelementtext('./ISN_CERTIFICATE_CL', a), '/CARD/CADRE_CERTIFICATE_CL/ISN_NODE16')[0]) if getelement('./ISN_CERTIFICATE_CL', a) else None,
                      getelementtext('ORDER_NUMBER', a) if getelement('ORDER_NUMBER', a) else getelementtext('DOCREASON_NUMBER', a),
                      element2date('ORDER_DATE', a) if getelement('ORDER_DATE', a) else element2date('DOCREASON_DATE', a))
                for a in self.getelementbyid(self.judgeid, '/CARD/CADRE_GOVERNMENTAWARD/ISN_PERSON57')]
                #for a in sorted(self.getelementbyid(self.judgeid, '/CARD/CADRE_GOVERNMENTAWARD/ISN_PERSON57'), key=partial(element2date, 'ORDER_DATE'))]
        
    def get_educations(self):
        return [Education(getelementtext('TITLE', e),
                           self.getelementtextbyid(id = getelementtext('ISN_RECEIVEDEDUCATION_CL', e),
                                                idpath =  '/CARD/CADRE_RECEIVEDEDUCATION_CL/ISN_NODE132',
                                                elementname = 'CLASSIF_NAME132')[0] if getelement('ISN_RECEIVEDEDUCATION_CL', e) else None,
                           element2date('DIPLOMA_DATE', e) if getelement('DIPLOMA_DATE', e) else element2date('GRADUATION_DATE', e),
                           getelementtext('SPECIALIZATION', e) if getelement('SPECIALIZATION', e) else None,
                           getelementtext('QUALIFICATION', e) if getelement('QUALIFICATION', e) else None)
                for e in self.getelementbyid(self.judgeid, '/CARD/CADRE_EDUCATION/ISN_PERSON46')]
                #for e in sorted(self.getelementbyid(self.judgeid, '/CARD/CADRE_EDUCATION/ISN_PERSON46'), key=partial(element2date, 'EDUCATION_BEGIN_DATE'))]
    
    def get_qualifier_class(self):
        for q in sorted(self.getelementbyid(self.judgeid, '/CARD/CADRE_QUALIFIERCLASS/ISN_PERSON126'), key=partial(element2date, 'CLASS_DATE'), reverse=True):
            return QC(self.getelementtextbyid(id = getelementtext('ISN_QUALIFIERCLASS_CL', q),
                                            idpath = '/CARD/CADRE_QUALIFIERCLASS_CL/ISN_NODE127',
                                            elementname = 'CLASSIF_NAME127')[0],
                      element2date('CLASS_DATE', q),
                      getelementtext('REASON', q))
        return QC(None, None, None)
    
    def get_prev_assignment(self):
        for q in sorted(self.getelementbyid(self.judgeid, '/CARD/CADRE_DISPLACEMENT/ISN_PERSON42'), key=partial(element2date, 'ASSIGNMENT_START_DATE'), reverse=True):
            return Assignment(element2date('ASSIGNMENT_START_DATE', q),
                              getelementtext('ASSIGNMENT', q))

    def get_job_history(self):
        job_place = self.getelementbyid(id = getelementtext('./ISN_ORGANIZATION_CL', self.person), idpath = '/CARD/CADRE_ORGANIZATION_CL/ISN_NODE114')[0]
        return [Job(getelementtext('./EMPLOYMENTPLACE', j),
                    getelementtext('./CITY', j) if getelement('./CITY', j) else None,
                    getelementtext('./WORKPLACE', j) if getelement('./WORKPLACE', j) else None,
                    element2date('./ACCEPTANCE_DATE', j),
                    element2date('./DISCHARGE_DATE', j))
                    for j in sorted(self.getelementbyid(self.judgeid, '/CARD/CADRE_LASTJOB/ISN_PERSON74'), key=partial(element2date, 'ACCEPTANCE_DATE'))] + [
                        Job(getelementtext('./CLASSIF_NAME114', job_place),
                            getelementtext('./ADDRESS', job_place),
                            self.getelementtextbyid(getelementtext('./ISN_STAFF', j), '/CARD/CADRE_STAFF/ISN_NODE154', 'OFFICE_SHORT')[0] if getelement('./ISN_STAFF', j) else None,
                            element2date('./ASSIGNMENT_START_DATE', j),
                            element2date('./DISMISSION_DATE', j) if getelement('./DISMISSION_DATE', j) else
                            element2date('./ASSIGNMENT_END_DATE', j) if getelement('./ASSIGNMENT_END_DATE', j) else None)
                            for j in sorted(self.tree.xpath('/CARD/CADRE_DISPLACEMENT[ISN_PERSON42="{}"][ISN_WORK42="{}"]'.format(self.judgeid, getelementtext('ISN_WORK174', self.job))),
                                            key=partial(element2date, 'ASSIGNMENT_START_DATE'))]
                    
    def write_avatar(self, path):
        for f in sorted(self.getelementbyid(self.judgeid, '/CARD/CADRE_FILE/ISN_PARENT'), key=partial(element2date, 'DOC_DATE'), reverse=True):
            if any(x in getelementtext('FILE_NAME', f) for x in ['jpg', 'jpeg', 'bmp', 'png']):
                file_id = getelementtext('ISN_FILE', f)
                file_ext = splitext(getelementtext('FILE_NAME', f))[-1]
                
                data = bytearray()
                for p in sorted(self.getelementbyid(file_id, '/CARD/CADRE_FILE_CONTENTS/ISN_FILE'), key=partial(element2int, 'PORTION')):
                    data += bytearray(base64.b64decode(getelementtext('CONTENTS', p)))
            
                file_name = '{}{}'.format(uuid.uuid4().hex, file_ext)
                with open('{}/{}'.format(path, file_name), 'wb') as f:
                    f.write(data)
                    
                return file_name
        return None
            
            
            