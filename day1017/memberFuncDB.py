import os
import sys
import pymysql
from day1016.sqlMember import *

def screen():
    print("### 간단한 회원 관리 프로그램 ###")
    print("0. 초기생성 1. 멤버추가 2. 멤버리스트 3. 멤버찾기 4. 정보수정 5. 화면지우기 6. 종료")

def dbConnection():
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='testdb', charset='utf8')
    curs = conn.cursor()
    return conn, curs

def createDBInit():
    conn,curs = dbConnection()

    curs.execute(sqlCreateDBInit, (temp1, temp1@naver.com, 100))
    curs.execute(sqlCreateDBInit, (temp1, temp1 @ naver.com, 100))
    curs.execute(sqlCreateDBInit, (temp1, temp1 @ naver.com, 100))

    conn.commit()
    conn.close()

def memberAdd():
    conn, curs = dbConnection()
    name = inFilter("->이름: ", 2)       #name = input("->이름: ")
    email = inFilter("->이메일: ", 2)     #email = input("->이메일: ")
    age = inFilter("->나이: ", 1)        #age = int(input("->나이: "))

    curs.execute(sqlMemberADD, (name, email, age))

    conn.commit()
    conn.close()

def memberAllList():    # Select절 구문 조건 없음
    print("\n-------- 회원정보 --------")
    print("이름 \t\t 이메일 \t\t 나이")
    conn,curs = dbConnection()
    curs.execute(sql)
    rows = curs.fetchall()

    for row in rows:
        print(row[0], '\t', row[1], '\t', row[2])

    conn.close()

    # for mem in memlist:
    #     print("%s\t%s\t %d" % (mem[0], mem[1], mem[2]))

def memberSearch():
    ser_name = inFilter("찾고싶은 사람 이름: ", 2)
    conn, curs = dbConnection()
    curs.execute(sql, ser_name)
    rows = curs.fetchall()
    for row in rows:
        print(row[0], '\t', row[1], '\t', row[2])
    conn.close()

    # for onemem in memlist:
    #     if ser_name in onemem:
    #         print("%s %s %d" % (ser_name, onemem[1], onemem[2]))
    #         break

def memberModify():
    ser_name = inFilter("찾고싶은 사람 이름: ", 2)
    conn,curs = dbConnection()
    curs.execute(sql, ser_name)
    rows = curs.fetchall()
    for row in rows:
        print(row[0], '\t', row[1], '\t', row[2])

    modiAge = input("변경할 나이 입력-> ")
    sql = """update testdb.member1 set age=%s where name=%s"""
    curs.execute(sql, modiAge, ser_name)
    print('%s남의 나이가 수정되었음!' % modiAge)
    conn.commit()
    conn.close()

    # for onemem in memlist:
    #     if ser_name in onemem:
    #         print("%s %s %d" % (ser_name, onemem[1], onemem[2]))
    #         break
    # print("-> %s, 이메일만 변경가능함" % onemem[1])
    # onemem[1] = inFilter("이메일 수정: ", 2)
    # print("변경 되었음.")

def inFilter(stmt, n):
    while (True):
        if n == 1: #문자체크
            choice = input(stmt)
            if choice.isalpha() == True or choice == '': pass
            else: return int(choice)
        elif n == 2: #숫자체크
            choice = input(stmt)
            if choice.isdigit() == True or choice == '': pass
            else: return choice
        elif n == 3: #메뉴숫자체크
            screen()
            choice = input(stmt)
            if choice.isalpha() == True or choice == '': pass
            else: return  int(choice)

def strInFilter(stmt):
    while (True):
        choice = input(stmt)
        if choice.isalpha() == True or choice == '':
            pass
        else:
            break
    return int(choice)

def intInFilter(stmt):
    while (True):
        value = input(stmt)
        if value.isdigit() == True or value == '':
            pass #os.system('cls')
        else:
            break
    return value

def menuInFilter(stmt):
    while (True):
        screen()
        choice = input(stmt)
        if choice.isalpha() == True or choice == '':
            pass
        else:
            break
    return int(choice)


if __name__== '__main__':
    memlist = []
    while True:
        choice = inFilter("-> ", 3)
        if choice == 0:
            createDBInit()
        elif choice == 1:
            memberAdd()
        elif choice == 2:
            memberAllList()
        elif choice == 3:
            memberSearch()
        elif choice == 4:
            memberModify()
        elif choice == 5:
            os.system("cls")
        elif choice == 6:
            sys.exit(1)
        else:
            print("잘못된 번호! 다시 입력바랍니다.")