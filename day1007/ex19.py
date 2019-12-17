# 1부터 50까지의 소수를 모두 출력하기
def prime(n):
    success = True
    for t in range(2, n, 1):
        if n % t == 0:
            return False
        return True

for t in range(2, 51 ,1):
    if prime(t) == True:
        print("%d " % t)

# 양의 정수 n을 입력 받아 그 이하의 모두 소수 출력하기
# 1부터 n까지의 소수의 개수 및 합 구하기
