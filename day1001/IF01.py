kor = input(input("국어 점수 :"))
eng = input(input("영어 점수 :"))
math = input(input("수학 점수 :"))

total = kor + eng + math
avg = total / 3

if avg <= 100 and avg >= 90:
    print("총점:%d 평균:%.2f, A+" % (total, avg))
elif avg <= 89 and avg >= 80:
    print("총점:%d 평균:%.2f, B+" % (total, avg))
elif avg <= 79 and avg >= 70:
    print("총점:%d 평균:%.2f, C+" % (total, avg))
elif avg <= 69 and avg >= 60:
    print("총점:%d 평균:%.2f, D+" % (total, avg))
else:
    print("총점:%d 평균:%.2f, F+" % (total, avg))