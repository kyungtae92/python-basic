n = int(input("어떤 수를 판별할까요? "))

for t in range(2, n, 1):
    if n % t == 0:
        print("%d는 %d로도 나누어지므로 소수가 아니다." % (n, t))
        break
    else:
        print("%d는 소수입니다." % n)
        print("1과 자기자신 %d로만 나누어집니다." % n)
        