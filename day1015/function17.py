# 리스트 반환


def initList(tempList):
    for i in range(1, 101):
        tempList.append(i)
    return tempList

def sumList(tempList):
    sum = 0
    for i in tempList:
        sum += i
    return sum

def main():
    tempList = []   #빈 리스트

    tempList = initList(tempList)
    print(tempList)
    sum = sumList(tempList)
    print(tempList, sum)

main()