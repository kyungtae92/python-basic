# 특정 입력받아서 리스트에 저장, 종료시 엔터키 입력

marvelNames = [] # 리스트 초기화

while True:
    name = input("마블 영웅 이름 입력(종료시 엔터키)>> ")

    if name == "":
        break

    marvelNames.append(name)

print("마블 영웅 리슽트: ")

for name in marvelNames:
    print(name, end=",")

for i in range(len(marvelNames)):
    print(marvelNames[i], end=" ")