# studentList = []
#
# studentList.append([100, 100, 100])
# studentList.append([90, 90, 90])
# studentList.append([80, 80, 80])
#
# print(studentList)
#
# for stu in studentList:
#     tot = 0
#
#     for score in stu:
#         tot += score
#
#     avg = tot / len(stu)
#     i = studentList.index(stu)
#     studentList[i].append(tot)
#     studentList[studentList.index(stu)].append(avg)
#
# print(studentList)




# 세 명의 점수 입력 받기~

studentListROW = []
studentListCOL = []
for i in range(0, 3):
    print(i+1, "번")
    for j in range(0, 3):
        studentListCOL.append(int(input(' 점수 입력: ')))

    studentListROW.append(studentListCOL)
    studentListCOL = []

for stu in studentListROW:
    tot = 0
    for score in stu:
        tot += score
    avg = tot / len(stu)
    stu.append(tot)
    stu.append(avg)

print(studentListROW)