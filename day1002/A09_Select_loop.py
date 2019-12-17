# 구구단 퀴즈 => 5문제, 사용자 정답,  2초내에 맞추어야 정답.

import random
import time

while True:
    jumsu = 0
    for t in range(5) :
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        dab = a * b
        print()

        startTime = time.time()     # 사용자 입력 시작점..시간 체크
        n = int(input("%d * %d = " % (a, b)))
        endTime = time.time()       # 사용자 입력 종료점..시간 체크
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
