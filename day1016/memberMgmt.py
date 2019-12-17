import os
import sys
# import  day1016.memberFunc as mfunc
from day1016.memberFunc import *

if __name__== '__main__':
    memlist = []
    while True:
        choice = inFilter("-> ", 3)
        if choice == 0:
            memlist = createNodeInit(memlist)
        elif choice == 1:
            memlist = memberAdd(memlist)
        elif choice == 2:
            memberAllList(memlist)
        elif choice == 3:
            memberSearch(memlist)
        elif choice == 4:
            memberModify(memlist)
        elif choice == 5:
            os.system("cls")
        elif choice == 6:
            sys.exit(1)
        else:
            print("잘못된 번호! 다시 입력바랍니다.")
