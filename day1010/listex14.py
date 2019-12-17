STUDENTS = 5

scoresList = [] # 학생들의 점수리스트
scoreSum = 0 # 총점

for i in range(STUDENTS):
    value = int(input("한명의 학생 총점: "))
    scoresList.append(value)
    scoreSum += value

scoreAvg = scoreSum / len(scoresList)

highScoreStudent = 0
for i in range(len(scoresList)):
    if scoresList[i] >= 80:
        highScoreStudent += 1

print("전체 평균은 ", scoreAvg)
print("80점이상의 학생수는 ", highScoreStudent, "명")
