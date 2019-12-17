def createNode():
    newNode = []
    return newNode

def newstudent(studentList):
    newNode = createNode()

    name = input('이름>> ')
    newNode.append(name)

    cnt = int(input('입력할 점수 개수>> '))
    for i in range(0, cnt):
        jum = int(input('%d번 점수>> ' % (i + 1)))
        newNode.append(jum)

    return  studentList.append(newNode)

def main():
    studentList = [] # 학생의 점수를 저장하는 리스트 초기화

    while True:
        newstudent(studentList)  # 새로운 학생 호출
        tot, avg = 0, 0

        for stu in studentList:
            tot = sum(stu[1:])  # tot = sum(stu[1:len(stu)])
            avg = tot / (len(stu)-1)

        stu.extend([tot, avg])

        ending = input('\n계속 입력(y/n)? ')
        if ending == 'Y' or ending == 'y':
            continue
        elif ending == 'N' or ending == 'n':
            break
        else:
            continue

    print("이름 점수1 점수2 총점 평균...")
    for sut in studentList:
        print(stu)
main()
