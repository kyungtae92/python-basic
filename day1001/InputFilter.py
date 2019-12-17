import os # 파이썬이 운영체제의 일부 기능을 가져옴(명령어 기반으로~)

while (True):
    s1 = input('number input plz...>> ')
    if s1.isalpha() == True or s1 == '':
        os.system('cls')
    else:
        break
s1 = int(s1)
print("%d + %d = %d" % (s1, 10, s1+10))
