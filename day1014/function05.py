import os

def floatValueIn():
    return float(input("실수범위 숫자입력: "))

def floatTotal(oneNumber, twoNumber):
    return oneNumber + twoNumber

def floatSubtraction(oneNumber, twoNumber):
    return oneNumber - twoNumber

def floatMultiplication(oneNumber, twoNumber):
    if oneNumber == 0 or twoNumber ==0:
        print('0으로 곱하는건 의미가 없습니다.')
        return 0
    else:
        return oneNumber * twoNumber

def floatDivision(oneNumber, twoNumber):
    if twoNumber == 0:
        print('0으로 나눌 수 없습니다.')
        return 0
    else:
        choice = int(input("1.몫 2.나머지>> "))
        if choice == 1:
            return oneNumber // twoNumber
        elif choice ==2:
            return oneNumber % twoNumber
        else:
            print('잘못선택')
            return 0

def menu():
    print('1.덧셈 2.뺄셈 3.곱셈 4.나눗셈 5.종료')
    menuNum = int(input("번호선택>> "))
    return menuNum
def main():
    oneNumber = floatValueIn()
    twoNumber = floatValueIn()

    menuNum = menu()

    if menuNum == 1:
        result = floatTotal(oneNumber, twoNumber)
        print("덧셈결과는 다음과 같습니다 ->", result)
    elif menuNum == 2:
        result = floatSubtraction(oneNumber, twoNumber)
        print("덧셈결과는 다음과 같습니다 ->", result)
    elif menuNum == 3:
        result = floatMultiplication(oneNumber, twoNumber)
        print("덧셈결과는 다음과 같습니다 ->", result)
    elif menuNum == 4:
        result = floatDivision(oneNumber, twoNumber)
        print("덧셈결과는 다음과 같습니다 ->", result)
    else:
        print("종료")
        return 0
main()