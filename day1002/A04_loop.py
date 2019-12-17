import os  # 파이썬이 운영체제의 일부 기능 가져옴(명령어)

while (True):
    dan = input('input gugudan >> ')
    if dan.isalpha() == True or dan == '':
        os.system('cls')
    else:
        break
dan = int(dan)
i = 0
for i in range(1, 10): # for i in range(1, 10, 1):
    print("%d * %d = %2d" % (dan, i, dan * i))
