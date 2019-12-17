# 글로벌 예약어 global

a = 20 # 전역변수

def func5():
    global a # 이 함수 안에서 a변수는 전역변수
    a = 10
    print('func5() a : ', a)


func5()