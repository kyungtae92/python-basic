str = "abcdefghijklmnopqrstuvwxyz"

for i in range(0,len(str),1):                   # 1번째 형태
    print("[%d] -> [%s]" % (i, str[i]))

for i in str:                                   # 2번째 형태
    print(i, end=",")