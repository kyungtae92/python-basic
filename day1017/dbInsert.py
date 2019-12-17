# DB에 데이터 저장하기

import pymysql

ser_memID = input('회원DB에 한명 추가-> ')
conn = pymysql.connect(host='localhost', user='root', password='1234', db='testdb', charset='utf8')

curs = conn.cursor()
sql = """insert into testdb.member(memID) 
         values (%s)"""

curs.execute(sql, (ser_memID))
# curs.execute(sql, (ser_memID))
# data = (('Jang'),
#         ('Jung'))
# curs.executemany(sql, data)

conn.commit()   # 실제 DB에 적용
print('추가 되었음!!!')
conn.close()
