import time

startTime = time.time()

name = input("당신의 이름을 영어로 입력하시오: ")

endTime = time.time()

dTime = endTime - startTime

print("영어 이름을 입력하는 %.2f초 걸렸습니다." % dTime)
