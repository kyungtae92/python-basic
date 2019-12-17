# 데이터베이스 스키마 정의
# 회원: idx, name, id, email, major
# idx - 번호(int 8자리)
# name - 이름(varchar(70))
# mid - 아이디(varchar(50))
# email - 메일주소(varchar(100))
# major - 전공분야(varchar(50))

# 요구사항, 인터페이스 정의, 설계(프로세스 설계, 데이터베이스 설계, 코드 설계) = 개발
import os
import sys
import pymysql

sqlMemReg = "insert into memberdb.member (name, mid, email, major) values (%s, %s, %s, %s)"
sqlMemAllList = "select * from memberdb.member"
sqlMemOneIdSrch = "select * from memberdb.member where mid=%s"
sqlMemOneEmailSrch = "select * from memberdb.member where email=%s"
sqlMemOneNameSrch = "select * from memberdb.member where name=%s"
sqlMemOneSearch = "select * from memberdb.member where mid=%s"
sqlMemOneSelect = "select * from memberdb.member where mid=%s"
sqlMemOneUpdate = "update memberdb.member set email=%s, major=%s where mid=%s"
sqlMemOneDelete = "delete from memberdb.member where mid=%s"

def dbConn():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='memberdb', charset='utf8')
    return conn

def displaymenu():
    print('### 회원 정보 관리 ###')
    print('1.회원등록 2.회원전체리스트 3.회원찾기 4.정보수정 5.회원삭제 6.화면클리어 7.종료')

def memRegister():
    global sqlMemReg

    name = input('이름: ')
    mid = input('아이디: ')
    email = input('이메일: ')
    major = input('전공분야: ')

    conn = dbConn()  # DB연결

    try:
        with conn.cursor() as curs:
            curs.execute(sqlMemReg, (name, mid, email, major))
        conn.commit()
        print('%s님이 추가되었음!' % (name))
    finally:
        conn.close()

def memAllListPtr():
    global sqlMemAllList

    print('---- 회원 전체 리스트 ----')
    print('번호\t\t이름\t\t아이디\t\t이메일\t\t\t전공분야')

    conn = dbConn()

    try:
        with conn.cursor() as curs:
            curs.execute(sqlMemAllList)
            rows = curs.fetchall()
            for row in rows:
                print(row[0], '\t\t', row[1], '\t', row[2], '\t', row[3], '\t', row[4])
    finally:
        conn.close()

def memOneSearch():
    srcChoice = input('1.찾는 아이디 2.찾는 이메일 3.찾는 이름\n-> ')
    conn = dbConn()

    try:
        with conn.cursor() as curs:
            if srcChoice == '1':
                schID = input('찾을 아이디: ')
                curs.execute(sqlMemOneIdSrch, schID)
            elif srcChoice == '2':
                schEmail = input('찾을 이메일: ')
                curs.execute(sqlMemOneEmailSrch, schEmail)
            elif srcChoice == '3':
                schName = input('찾을 이름: ')
                curs.execute(sqlMemOneNameSrch, schName)
            else:
                return
            rows = curs.fetchall()
            if rows:
                for row in rows:
                    print('\t'.join(map(str, row)))
            else:
                print("찾을 수 없음")
                return
    finally:
        conn.close()

def memInfoModify():
    global sqlMemOneSelect
    global sqlMemOneUpdate

    schID = input('찾고싶은 아이디: ')

    conn = dbConn()

    try:
        with conn.cursor() as curs:
            curs.execute(sqlMemOneSelect, schID)
            rows = curs.fetchall()
            if rows:
                for row in rows:
                    print(row[0], '\t\t', row[1], '\t', row[2], '\t', row[3], '\t', row[4])
                    modiEmail = input('수정할 이메일: ')
                    modiMajor = input('수정할 전공분야: ')
                    curs.execute(sqlMemOneUpdate, (modiEmail, modiMajor, schID))
                    conn.commit()
                    print("%s 회원 정보 수정완료" % schID)
            else:
                print("찾는 정보 없음")
                return
    finally:
        conn.close()

def memInfoDelete():
    global sqlMemOneDelete
    global sqlMemOneSelect

    schID = input('삭제할 아이디: ')

    conn = dbConn()

    try:
        with conn.cursor() as curs:
            curs.execute(sqlMemOneSelect, schID)
            rows = curs.fetchall()
            if rows:
                for row in rows:
                    print(row[0], '\t\t', row[1], '\t', row[2], '\t', row[3], '\t', row[4])
                    delok = input('삭제 하시겠습니까(Y/N)?')
                    if delok == 'Y' or delok == 'y':
                        curs.execute(sqlMemOneDelete, schID)
                        conn.commit()
                        print("%s 회원 아이디 삭제" % schID)
                    elif delok == 'N' or delok == 'n':
                        print("%s 회원 삭제 취소" % schID)
                        return
            else:
                print("찾는 아이디 없음")
                return
    finally:
        conn.close()

if __name__ == '__main__':
    while True:
        displaymenu()
        choice = input('-> ')

        if choice == '1':
            memRegister()
        elif choice == '2':
            memAllListPtr()
        elif choice == '3':
            memOneSearch()
        elif choice == '4':
            memInfoModify()
        elif choice == '5':
            memInfoDelete()
        else:
            pass