def main():
    while True:
        coffee = int(input('어떤 커피(1.보통 2.설탕 3.블랙 4.종료): '))

        if coffee == 4:
            break
        else:
            coffee_machine(coffee)

def coffee_machine(coffee):
    print('#1. 뜨거운 물을 준비한다.')
    print('#2. 종이컵을 준비한다.')

    if coffee == 1:
        print("보통 커피를 탄다.")
    elif coffee == 2:
        print("설탕 커피를 탄다.")
    elif coffee == 3:
        print("블랙 커피를 탄다.")
    else:
        print('#아무거나 탄다.')

    print("#4. 뜨거운 물을 붓는다.")
    print("#5. 스푼으로 젓는다.")
    print()
    print("손님한테 커피를 드린다.")

main()