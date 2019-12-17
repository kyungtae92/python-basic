def printGuGuDan(dan):
    i = 1
    while(i<=9):
        print("%d * %d = %d" % (dan, i, dan*i))
        i = i + 1

def main():
    dan = int(input("구구단 입력>> "))
    printGuGuDan(dan)
    print("%d단 출력 완료!!" % dan)

main()