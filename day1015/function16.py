# 리스트 반환

def listSum(tempList):
    print(tempList, id(tempList))
    sum = 0
    for i in tempList:
        sum = sum + i
    return sum

def main():
    tempList = [1,2,3,4,5,6,7,8,9,10]
    print(tempList, id(tempList))

    sum = listSum(tempList)   # 함수 매개변수에 리스트값을 넘김
    print(tempList, "->", sum)

main()