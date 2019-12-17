# 리스트 문자열에서 인덱스를 이용한 출력

text = "Will is power"
print(text[0], text[3], text[-1])

flist = ["apple", "banana", "tomato", "peach", "pear"]
print(flist[0], flist[3], flist[-1])

# 리스트 또는 문자열에서 슬라이싱에서 원하는 범위만큼 출력
sqr = [0,1,4,9,16,25,35,49]
print(sqr[3:6])
print(sqr[3:])

# 리스트 두개 합치기
marvel = ['스파이더맨', '토르', '아이언맨']
dc = ['슈퍼맨', '베트맨', '아쿠아맨']

heros = marvel + dc # 문자열 합치기
print(heros)

for name in heros:
    print(name)

# 리스트를 연속적인 숫자만큼 추가하기
values = [1,2,3] * 3
print(values)