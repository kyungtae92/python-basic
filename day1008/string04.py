# 문자열의 모든 글자 뒤에 $를 붙여서 출력

ss = "파이썬짱!"

sslen = len(ss)   # 문자열이 길이 값을 숫자로 알 수 있음

for i in range(0, sslen):   # for i in range(0, len(ss)):  옆에 문법과 같음.
    print(ss[i] + '$', end=' ')





# 원래 코딩
# ss = "파이썬짱!"
# temp = ss
#
# for i in temp:
#     print(temp[i])