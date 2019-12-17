n = int(input("어떤 수를 판별할까요? "))
success = True

for t in range(2, n, 1):        # t = 2 -> while t < n:
    if n % t == 0:
        success = False
        break
if success == True:
    print("%d는 소수 입니다." % n)
else:
    print("%d는 소수아니다." % n)