# 체질량지수 BMI 계산하여 건강 진단하기
# BMI = 몸무게 / 키 * 키

height = int(input("키가 몇 cm입니까? "))
weight = int(input("몸무게가 몇 km입니까?: "))

height = height / 100
bmi = weight / (height * height)        # bmi = weight / (height ** 2)

print("당신의 체질량지수는 %.2f" % bmi)

if bmi < 20 :
    print("저체중입니다.")
elif 20 <= bmi < 25 :           # bmi >= 20 and bmi < 25
    print("정상체중입니다.")
elif 25 <= bmi < 30 :
    print("경도비만입니다.")
elif 30 <= bmi < 40 :
    print("비만입니다.")
elif 40 <= bmi:
    print("고도비만입니다.")
