# 문자열 함수 -> 대문자 소문자 변환하기 함수
# upper(), lower(), swapcase(), title()

ss = 'Python is Easy. 그래서 programming이 재미있습니다.'

up = ss.upper()
print(up)

lo = ss.lower()
print(lo)

sw = ss.swapcase()    # 소문자를 대문자로 대문자를 소문자로 동시에 변환
print(sw)

ti = ss.title()       # 단어의 앞 글자만 대문자로 변환
print(ti)