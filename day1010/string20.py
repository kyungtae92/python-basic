# 문자열 채우기

ss = "파이썬"

print(ss.center(11))
print(ss.center(11, '-'))
print(ss.ljust(11))
print(ss.rjust(11))
print(ss.zfill(11))

# 문자열 형식,형태,구성
s1 = "1234"
print(s1.isdigit())  #현재 문자열이 숫자형식인지?

s2 = "abcd"
print(s2.isalpha())  #현재 문자열이 알파벳인지?

s3 = "abcd123"
print(s3.isalnum())  #현재 문자열이 숫자,알파벳 혼합인지?

s4 = "    "
print(s4.isspace())  #현재 문자열에 공백이 있는지?

