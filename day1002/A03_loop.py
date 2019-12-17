# 구구단
i = 0; dan = 0
dan = int(input('출력할 한개의 단을 입력> '))

for i in range(1, 10): # for i in range(1, 10, 1): 1은 생략가능
    print("%d * %d = %2d" % (dan, i, dan*i))

k = 0; ddan = 0
ddan = int(input('출력할 한개의 단을 입력> '))
while k < 10:
    print("%d * %d = %2d" % (ddan, k, ddan * k))
    k = k + 1