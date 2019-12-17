import pymysql

modiID = input('수정할 ID: ')
modiStr = input('수정할 값: ')


conn = pymysql.connect(host='localhost', user='root', password='1234', db='testdb', charset='utf8')
curs = conn.cursor()

sql = """update testdb.member set memID =%s where memID=%s"""
curs.execute(sql, (modiStr, modiID))

conn.commit()
print('수정 되었음')
conn.close()