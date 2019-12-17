# 키에 적당한 몸무게
# 적정몸무게 = (키 - 100) * 0.9
# 과체중 위험 기준 = 적정몸무게 * 1.2
# 저체중 위험 기준 = 적정몸무게 * 0.8

key = float(input("키가 몇 cm에요?"))

stan = (key - 100) * 0.9
print("당신의 신장: ", key)
print("적정 몸무게: ", stan)

over = stan * 1.2
under = stan * 0.8
print("과체중 위험 기준: ", over)
print("저체중 위험 기준: ", under)