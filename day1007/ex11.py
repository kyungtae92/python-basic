# 주차요금 계산하기

print("=== 주차료 계산 프로그램===")
parkingTime = int(input("주차시간 입력 : "))

unitT = parkingTime // 15

fee = unitT * 1000

print("주차시간 : ", parkingTime, "분")
print("주차요금 : ", fee, "원")