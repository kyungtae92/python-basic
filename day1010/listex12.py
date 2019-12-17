
scoresList = []
sum = 0
for i in range(10):
    # jumsu = int(input('과목 점수를 입력: '))
    # scoresList.append(jumsu)
    scoresList.append(int(input('과목 점수를 입력: ')))

# for i in scoresList:          1
#     sum = sum + i

for i in range(10):             #2
    sum = sum + scoresList[i]
    print(sum)