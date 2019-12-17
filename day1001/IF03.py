# 문자열 판단 가능함.

userID = "qwert1234"
userPWD = "1234567890"
inID = input("사용자 ID입력: ")
inPWD = input("패스워드 입력: ")

if inID == userID and inPWD == userPWD:         # 유형1
    print("아이디가 일치합니다.", inID)
    print("패스워드가 일치합니다.", inPWD)
else:
    print("아이디 또는 패스워드가 불일치함.")


if inID == userID:                              # 유형2
    if inPWD == userPWD:
        print("아이디 패스가 전부 일치")
    else:
        print("패스워드 불일치")
else:
    print("아이디가 불일치")
