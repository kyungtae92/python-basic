# 문자열 중간의 공백까지 삭제

inStr = "   한글 Python 프로그래밍   "
outStr = ""

for i in range(0, len(inStr)):
    if inStr[i] != ' ':
        outStr += inStr[i]

print("원래 문자열: [%s] " % inStr)
print("공백제거 문자열: [%s] " % outStr)

