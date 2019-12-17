# 검색 쿼리에 조건절 포함

import pymysql

ser_name = input('검색할 회원 ID-> ')

conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='testdb', charset='utf8')

curs = conn.cursor()
sql = "select * from member where memID=%s"
curs.execute(sql, ser_name)

rows = curs.fetchall()
for row in rows:
    print(row[0], row[1]) # print(row['idx'], row['memID']) # print(row)

conn.close()
