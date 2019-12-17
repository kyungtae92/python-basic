import pymysql

delID = input('삭제할 ID: ')

conn = pymysql.connect(host='localhost', user='root', password='1234', db='testdb', charset='utf8')
curs = conn.cursor()

sql = """delete from member where memID=%s"""
curs.execute(sql, delID)
conn.commit()

print('삭제 되었음')
conn.close()