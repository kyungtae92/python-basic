# 문자열 함수 count(), find(), index()

ss ="Process finished with exit code"

# count()  -> 문자열 범위에서 찾고자하는 문자가 몇 개 있는지
res = ss.count('i')
print(res)
res = ss.count('sh')
print(res)

# find()    -> 문자열에서 문자를 찾음(그 단어가 시작하는 위치값)
res = ss.find('cess')
print(res)

# index()    -> find와 비슷한 개념
res = ss.index('with')
print(res)

# startswith()   -> 그 단어가 시작할 때는 있으면 True 없으면 False
res = ss.startswith('Process')
print(res)
res = ss.startswith('exit')
print(res)

# endswith()  -> 그 단어가 마지막부분에 있으면 True 없으면 False
res = ss.endswith('hello')
print(res)
res = ss.endswith('code')
print(res)

