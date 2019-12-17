# 2.암호화 예제 : 두 사람만의 비밀 편지
# 편지 암호화
# 원문을 입력받아 암호화 문장으로 변경하시오. 조건은 각 문자에 해당하는 숫자에 단순히 1을 더하는 암호화 방식으로 할 것.

# letter1 = 'A'
# letter1 = ord(letter1)
# print(letter1)

# letter2 = 'B'
# letter2 = (ord(letter2) + 1)
# print(letter2)

# letter3 = 'B'
# letter3 = chr(ord(letter3) + 1)
# print(letter3)


# 방법1 .반복문 이용
letter = "HELLO PYTHON"
encode = ""

for ch in letter:
    num = ord(ch)
    encode = encode + chr(num + 1)

print("원문: ", letter)
print("암호: ", encode)


# 방법2
# letter = "HELLO PYTHON"
# encode = ""
# ch1 = letter[0]
# ch2 = letter[1]
# ch3 = letter[2]
# ch1 = ord(ch1)+1
# ch2 = ord(ch2)+1
# ch3 = ord(ch3)+1
# encode = encode + chr(ch1) + chr(ch2) + chr(ch3)
# print(encode)
#
# letter = input("암호할 문자열 입력: ")
# encode = ""
# for ch in letter:
#     num = ord(ch)
#     encode = encode + chr(num + 1)
#
# print("원문: ", letter)
# print("암호: ", encode)
