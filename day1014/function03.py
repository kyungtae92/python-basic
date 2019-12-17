# 함수1 : 매개변수가 O 리턴(반환값) X
# 함수2 : 매개변수가 X 리턴(반환값) O
# 함수3 : 매개변수가 O 리턴(반환값) O
# 함수4 : 매개변수가 X 리턴(반환값) X

# 파이썬 함수 구성 : def 함수명(매개변수):
#                       return (변수, 값, 레퍼런스) 다 올 수 있음

def func01(intvalue, strName, floatPI):
    print(intvalue, strName, floatPI)

def func02():
    # sGrade = input("학점 입력: ")
    # return sGrade
    return input("학점 입력: ")
def func03(floatAvg):
    # result = ''
    if floatAvg >= 90:
        return 'A'  # result = 'A'
    elif 89 >= floatAvg <= 80:
        return 'B'  # result = 'B'
    else:
        return 'C,D,F'  # result = 'C,D,F'
    # return result

def displayMenu():
    print("1. 새게임")
    print("2. 저장게임")
    print("3. 설정")
    print("4. 종료")
    print("선택>> ")

def main():
    func01(100, 'Kim', 3.14)
    print(func02())  #sGrade = func02()
    hakjum = func03(float(input('평균값을 입력: ')))
    print(hakjum)

main()