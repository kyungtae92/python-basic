class Contact:
    def __init__(self, name, phone_number, e_mail, addr):
        self.name = name
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.addr = addr

    def print_info(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("E-mail: ", self.e_mail)
        print("Address: ", self.addr)

def set_contact():  #클래스 내부에 입력하는 함수
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    e_mail = input("E-mail: ")
    addr = input("Address: ")

    contact = Contact(name, phone_number, e_mail, addr)
    return contact

def defalutIn(contact_list):
    contact_list.append( Contact('Moon', '010-222-333', 'Moon@gmail.com', 'Seoul') )
    contact_list.append(Contact('kim', '010-111-3555', 'kim@gmail.com', 'Pusan'))
    contact_list.append(Contact('Hong', '010-333-777', 'Hong@gmail.com', 'DaeGu'))

def print_menu():
    print("1. 연락처 입력  2. 연락처 출력  3. 연락처 삭제  4. 종료")
    menu = input("메뉴선택: ")
    return int(menu)
def printdisplay(contact_list):
    for i in contact_list:
        i.print_info()

def run():
    contact_list = []
    while 1:
        menu = print_menu()
        if menu == 0:
            contact = defalutIn(contact_list)
        elif menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu == 2:
            printdisplay(contact_list)
        elif menu == 4:
            break

if __name__ == "__main__":
    run()