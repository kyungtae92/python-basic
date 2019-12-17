def func1():
    a = 10  # func1()에서만 적용되는 지역변수(Local Variable)
    print("func1() a: ", a)
    a = 10 + 20
    print("func1() a: ", a)

def func2():
    print('func2() a: ', a)     # a변수가 선언되어 있지 않아서

a = 100     # 전역변수 - 이 파일 전체에 적용되는 변수

func1()
func2()