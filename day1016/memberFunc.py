import os
import sys

def screen():
    print("### 간단한 회원 관리 프로그램 ###")
    print("0. 초기생성 1. 멤버추가 2. 멤버리스트 3. 멤버찾기 4. 정보수정 5. 화면지우기 6. 종료")

def createNodeInit(memlist):
    newNode = createNode()
    newNode.append("KIM")
    newNode.append("chris24000@naver.com")
    newNode.append("28")

    memlist.append(newNode)
    return memlist

def createNode():
    netNode = []
    return netNode

def memberAdd(memlist):
    netNode = createNode()
    name = inFilter("->이름: ", 2)       #name = input("->이름: ")
    netNode.append(name)
    email = inFilter("->이메일: ", 2)     #email = input("->이메일: ")
    netNode.append(email)
    age = inFilter("->나이: ", 1)        #age = int(input("->나이: "))
    netNode.append((age))
    memlist.append(netNode)
    return memlist

def memberAllList(memlist):
    print("-------- 정보 --------")
    print("이름\t\t이메일\t\t\t나이")
    for mem in memlist:
        print("%s\t%s\t %d" % (mem[0], mem[1], mem[2]))

def memberSearch(memlist):
    ser_name = inFilter("찾고싶은 사람 이름: ", 2)
    for onemem in memlist:
        if ser_name in onemem:
            print("%s %s %d" % (ser_name, onemem[1], onemem[2]))
            break

def memberModify(memlist):
    ser_name = inFilter("찾고싶은 사람 이름: ", 2)
    for onemem in memlist:
        if ser_name in onemem:
            print("%s %s %d" % (ser_name, onemem[1], onemem[2]))
            break
    print("-> %s, 이메일만 변경가능함" % onemem[1])
    onemem[1] = inFilter("이메일 수정: ", 2)
    print("변경 되었음.")

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
