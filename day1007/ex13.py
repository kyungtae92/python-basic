curtime = int(input("지금 몇시인가요? "))
pretime = curtime - 6
if pretime < 0:
    pretime += 24
print("현재 시간: %d시" %curtime)
print("이전 시간: %d시" %pretime)
