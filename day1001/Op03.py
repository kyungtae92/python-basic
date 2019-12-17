# 달러 환전액 , 1달러가 1,175원
# 250달러 환전 몇달러?

money = 2500000
cost = 1175
proc = money // cost
other = money % cost

print("가진돈 : ", money, "원")
print("환율 : ", cost, "원")
print("환전액 : ", proc, "달러")
print("남은돈 : ", other, "원")

