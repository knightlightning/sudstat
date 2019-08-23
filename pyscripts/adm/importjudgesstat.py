#!/usr/bin/python3

'''
Created on 27 окт. 2017 г.

@author: kmironov
'''

from sqlalchemy import and_
from datetime import datetime
import enum
import sys
sys.path.append('/usr/share/sudstat')
from pyscripts.sudstatdb import *
from pyscripts.conn import *
from sse import *

courts = [
    ('firebird+fdb://sysdba:77@10.55.48.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Кировский районный суд',[0,1]),
    ('firebird+fdb://sysdba:77@10.55.87.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Кировский районный суд',[2]),
    ('firebird+fdb://sysdba:m@10.55.49.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Куйбышевский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:xxx@10.55.50.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Ленинский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.51.42:49152/D:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Октябрьский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:masterkey@10.55.54.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Центральный районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.53.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Советский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:1@10.55.52.42:49152/E:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Первомайский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:masterkey@10.55.55.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Азовский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.56.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Большереченский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:masterkey@10.55.57.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Большеуковский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.58.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Горьковский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.59.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Знаменский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.60.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Исилькульский городской суд',[0,1,2]),
    ('firebird+fdb://sysdba:masterkey@10.55.61.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Калачинский городской суд',[0,1,2]),
    ('firebird+fdb://sysdba:masterkey@10.55.62.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Колосовский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.63.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Кормиловский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.64.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Крутинский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.66.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Любинский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:masterkey@10.55.65.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Марьяновский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.67.42:49152/C:/DATA/UNI_WORK2003.GDB?charset=win1251','Москаленский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.68.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Муромцевский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.69.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Называевский городской суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.70.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Нижнеомский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.71.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Нововаршавский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.72.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Одесский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:masterkey@10.55.74.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Оконешниковский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.73.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Омский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:masterkey@10.55.75.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Павлоградский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.76.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Полтавский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:masterkey@10.55.77.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Русско-Полянский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:masterkey@10.55.78.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Саргатский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.79.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Седельниковский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.80.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Таврический районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.81.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Тарский городской суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.82.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Тевризский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.83.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Тюкалинский городской суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.84.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Усть-Ишимский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.85.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Черлакский районный суд',[0,1,2]),
    ('firebird+fdb://sysdba:m@10.55.86.42:49152/C:/DATA/JUSTICE/UNI_WORK2003.GDB?charset=win1251','Шербакульский районный суд',[0,1,2])
]

class ProcudureType(enum.Enum):
    adm = 0
    civ = 1
    crim = 2

class MyEnum(enum.Enum):
    @classmethod
    def getValueByKeyName(cls, key):
        return cls.__members__[key].value

class ChargeClasses(MyEnum):
    adm = (AdmCharge, AdmChargeData, AdmStatType)
    civ = (CivCharge, CivChargeData, CivStatType)
    crim = (CrimCharge, CrimChargeData, CrimStatType)

class JudgeQueries(MyEnum):
    adm = "SELECT judge_name FROM sys_judge_list('[G1]', 1, null) WHERE judge_id = {}"
    civ = "SELECT judge_name FROM sys_judge_list('[G1]', 1, null) WHERE judge_id = {}"
    crim = "SELECT judge_name FROM sys_judge_list('[U1]', 1, null) WHERE judge_id = {}"

def getCharge(court_id, chargeClass, curr_date, session):
    res = session.query(chargeClass).filter(and_(chargeClass.court_id == court_id, chargeClass.year == curr_date.year)).first()
    if res == None:
        charge = chargeClass(year=curr_date.year, court_id=court_id, modification=datetime.now().date())
        session.add(charge)
        session.commit()
        return charge
    return res

def getJudge(court_id, ext_id, conn, chargeType, session):
    res = session.query(Judge).filter(and_(Judge.court_id == court_id, Judge.ext_id == ext_id)).first()
    if res == None:
        ext_judge = conn.execute(JudgeQueries.getValueByKeyName(chargeType).format(ext_id)).fetchone()
        judge = Judge(court_id = court_id, ext_id = ext_id, name = ext_judge[0])
        session.add(judge)
        session.commit()
        return judge
    return res

def stream(curr_date):
    class ChargeQueries(MyEnum):
        adm = '''SELECT row_id, column_id, count(*)
FROM g1_aq_cases_1('{}-01-01', '{}', '[P1]')
WHERE row_id <> 0 AND row_id <> -1
GROUP BY row_id, column_id'''.format(curr_date.year, curr_date)
        civ = '''SELECT row_id, column_id, count(*)
FROM g1_aq_total_finish_1('{}-01-01', '{}', 1)
WHERE row_id <> 0 AND row_id <> -1
GROUP BY row_id, column_id'''.format(curr_date.year, curr_date)
        crim = '''SELECT row_id, column_id, count(*)
FROM u1_aq_total_finish_1('{}-01-01', '{}')
WHERE row_id <> 0 AND row_id <> -1
GROUP BY row_id, column_id'''.format(curr_date.year, curr_date)

    session = get_session(sudstat)

    for court in courts:
#        if 'Называевский' not in court[1]:
#            continue
        yield print_sse(SSEType.info, 'Court "{}" is being processed...'.format(court[1]))
        try:
            engine = create_engine(court[0], pool_timeout=10)
            with engine.connect() as remote_conn:
                court_id = session.query(Court.id).filter(Court.name == court[1]).one().id
                for proc in [ProcudureType(i).name for i in court[2]]:
                    yield print_sse(SSEType.info, 'Procedure "{}" is being processed...'.format(proc))
                    try:
                        res = remote_conn.execute(ChargeQueries.getValueByKeyName(proc))
                        chargeCls, chargeDataCls, chargeStatTypeCls = ChargeClasses.getValueByKeyName(proc)
                        charge = getCharge(court_id, chargeCls, curr_date, session)
                        for judge_id, stat_type, stat_val in res:
                            #print(judge_id,stat_type,stat_val)
                            data = charge.data.filter(and_(chargeDataCls.judge_ext_id == judge_id, chargeDataCls.stat_type_id == stat_type)).first()
                            if data == None:
                                judge = getJudge(court_id, judge_id, remote_conn, proc, session)
                                stat_types = session.query(chargeStatTypeCls.id).all()
                                for t in stat_types:
                                    data = chargeDataCls(charge=charge, judge=judge, stat_type_id=t, data=stat_val if stat_type == t.id else None)
                                    charge.data.append(data)
                            else:
                                data.data = stat_val
                            charge.modification = curr_date
                            session.commit()
                        yield print_sse(SSEType.info, 'Procedure "{}" has been processed!'.format(proc))
                    except Exception as e:
                        yield print_sse(SSEType.error, 'There\'s error while handling "{}" procedure: {}'.format(proc, e))
                yield print_sse(SSEType.info, 'Court "{}" has been processed!'.format(court[1]))
        except Exception as e:
            yield print_sse(SSEType.error, 'There\'s error while handling "{}" court: {}'.format(court[1], e))

    yield print_sse(SSEType.info, 'Everything is done.')
    yield print_sse(SSEType.system, 'END-OF-STREAM')

from flask import Flask
from flask import Response
application = Flask(__name__)

@application.route("/wsgi-bin/importjudgesstat/<mydate>")
def app(mydate):
    d = datetime.strptime(mydate, '%Y-%m-%d')
    return Response(stream(d), mimetype="text/event-stream")

@application.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == "__main__":
    application.run()
