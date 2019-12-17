def iniList(eList, oList):
    for i in range(1, 101, 2):
        oList.append(i)
    for i in range(0, 101, 2):
        eList.append(i)

    return eList, oList

def main():
    eList = []
    oList = []

    eList, oList = iniList(eList, oList)
    print(eList)
    print(oList)

main()