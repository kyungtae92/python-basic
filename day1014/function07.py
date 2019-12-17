def primeInValue()
    x = int(input('첫 번째 숫자 입력(작은수: '))
    y = int(input('두 번째 숫자 입력(큰수: '))
    return x, y

def primeOperating(x, y):
    for i in range(x, y + 1):  # 두 숫자 사이를 반복
        for j in range(2, int(x / 2)):  # 하나의 숫자에 대해 2부터 숫자의 반까지 반복
            if i % j == 0:
                break
            else:
                print(i, end=' ')  # 소수 출력
                count = count + 1
        else:
            print()

        return count


def printPrime(count)
    print('소수는 모두 ', count, '개 입니다')

def main():
    x, y = primeInValue()
    count = 0
    print(x, '부터', y, '사이의 소수: ', end=' ')
    count = primeOperating(x, y)
    printPrime(count)

main()