#_*_coding=utf-8_*_
#__author__='xj'
'use for extra target'
import sqlite3

class ExtraData(object):
    def extraExtSysId(self):
        conn = sqlite3.connect('zh.db')
        cursor = conn.cursor()
        cursor.execute('select ext_sys_id,userid from extsysid_userid where ext_sys_id in ('
                       'select ext_sys_id from extsysid_userid where '
                       'channel_id =1000 group by ext_sys_id having count(userid) >1) order by ext_sys_id ')
        values = cursor.fetchall()
        print('%s,valuse:%s)'%(ExtraData.extraExtSysId,values))
        cursor.close()
        conn.close()
        return values

    def filterLogoned(self,userid):
        conn = sqlite3.connect('zh.db')
        cursor = conn.cursor()
        sql = "select userid from user_logon where userid in"
        s=''
        for id in userid:
            s = s + str(id) + ','
        sql = sql + '(' + s[:-1] + ')'
        print('sql %s'%sql)
        cursor.execute(sql)
        values = cursor.fetchall()
        print('%s,valuse:%s)' % (ExtraData.filterLogoned, values))
        cursor.close()
        conn.close()
        return values

def unitTest():
    extra = ExtraData()
    extra.extraExtSysId()
    extra.filterLogoned([300733518,400733511])

unitTest()