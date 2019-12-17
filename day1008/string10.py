# 문자열을 입력하다보면 공백이 들어감
# strip()  -> 문자열 양 끝에 공백을 제거함

ss = ' 파 이 썬 '

print(ss)
res = ss.strip()
print(res)

res = ss.rstrip()
print(res)

res = ss.lstrip()
print(res)
