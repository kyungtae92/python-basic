# 1. 반복 기초 예제 - loopbasic
# 2. 구구단 한단만 출력 - oneGuGudan
# 3. 콘솔 재입력 예제 - consoleInput
# 4. 전체 구구단 출력 - gugudanFull
# 5. 별모양 출력 - starPrint
# 6. 삼각형 별모양 출력 - trianglePrint
# 7. 구구단 게임 - gameGuGuDan
# 8. 종료
import os
import random
import time

def loopbasic():
    for i in range(1, 101, 2):
        print(i, end=' ')
    print('\n')
    for i in range(0, 101, 2):
        print(i, end=' ')
    print('\n')
    for i in [1, 2, 3, 4, 5]:
        print(i, end=' ')
    i = 50
    while (i > 0):
        print(i, end=' ')
        i = i - 1
    print('\n')

    for k in range(50, -1, -1):
        print(k, end=' ')

def oneGuGudan():
    i = 0;
    dan = 0
    dan = int(input('출력할 한개의 단을 입력> '))

    for i in range(1, 10):  # for i in range(1, 10, 1): 1은 생략가능
        print("%d * %d = %2d" % (dan, i, dan * i))

def consoleInput():
    while (True):
        dan = input('input gugudan >> ')
        if dan.isalpha() == True or dan == '':
            os.system('cls')
        else:
            break
    dan = int(dan)
    i = 0
    for i in range(1, 10):  # for i in range(1, 10, 1):
        print("%d * %d = %2d" % (dan, i, dan * i))


def gugudanFull():
    dan = 2

    while dan <= 9:
        print("===", dan, "단 ===")
        i = 1

        while (i <= 9):
            print(dan, "*", i, "=", dan * i)
            i = i + 1

        dan = dan + 1
    print("-------------------------------")

    dan = 2
    while dan <= 9:
        print("===", dan, "단 ===")
        for i in range(1, 10):
            print(dan, "*", i, "=", dan * i)
        dan = dan + i
    print("-------------------------------")

    dan = 2
    for dan in range(2, 10):
        print("===", dan, "단 ===")
        for i in range(1, 10):
            print(dan, "*", i, "=", dan * i)
    print("-------------------------------")

    for i in range(1, 10):
        for j in range(2, 10):
            print("%d*%d=%2d " % (j, i, j * i), end=' ')
        print("\n")


def starPrint():
    x = int(input("출력할 별 수 입력>> "))
    for i in range(1, x + 1):
        for j in range(x - i):
            print(' ', end='')

        for k in range(i):
            print("*", end='')
        print()


def trianglePrint():
    x = int(input("출력할 별 수 입력>> "))
    for i in range(1, x + 1):
        for j in range(x + 1 - i):
            print(' ', end='')

        for k in range(2 * i - 1):
            print("*", end='')
        print()


def gameGuGuDan():
    while True:
        jumsu = 0
        for t in range(5):
            a = random.randint(2, 9)
            b = random.randint(2, 9)
            dab = a * b
            print()

            startTime = time.time()  # 사용자 입력 시작점..시간 체크
            n = int(input("%d * %d = " % (a, b)))
            endTime = time.time()  # 사용자 입력 종료점..시간 체크
            totalTime = endTime - startTime  # 정답 입력한 시간 계산

            if n == dab:
                if totalTime <= 2:
                    jumsu = jumsu + 1
                    print("맞췄습니다!")
                else:
                    print("정답이긴 하나 시간이내 맞추지 못했습니다ㅠㅠ")
            else:
                print("땡!~ 틀렸습니다!")
        print("당신의 점수는 %d점 입니다." % (jumsu * 20))
        print()
        play = input("구구단 게임을 다시 해보시겠습니까(y/n)?")
        if play == 'y' or play == 'Y':
            continue
        elif play == 'n' or play == 'N':
            print("게임을 종료합니다.")
            break

def menudisplay():
    print('\n1. 반복 기초 예제')
    print('2. 한개 구구단 출력')
    print('3. 콘솔 재입력 예제')
    print('4. 전체 구구단 출력')
    print('5. 별모양 출력')
    print('6. 삼각형 별모양 출력')
    print('7. 구구단 게임')
    print('8. 종료')
    print('선택-> ', end='')

def main():
    while True:
        menudisplay()
        choice = int(input())

        if choice == 1:
            loopbasic()
        elif choice == 2:
            oneGuGudan()
        elif choice == 3:
            consoleInput()
        elif choice == 4:
            gugudanFull()
        elif choice == 5:
            starPrint()
        elif choice == 6:
            trianglePrint()
        elif choice == 7:
            gameGuGuDan()
        elif choice == 8:
            print("프로그램 종료!!!!")
            break
        else:
            print("번호 잘못입력 되었습니다.")

main()
