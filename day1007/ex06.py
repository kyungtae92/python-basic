# 번역

# import webbrowser
#
# text = input("번역할 문장을 입력하시오: ")
#
# url = "http://translate.google.co.kr/#ko/en/" + text        # 한국어
# webbrowser.open(url)
#
# #url = "http://translate.google.co.kr/#ko/ja/" + text        # 일본어
# #webbrowser.open(url)
#
# #url = "http://translate.google.co.kr/#ko/zh-CN/" + text     # 중국어
# #webbrowser.open(url)


import webbrowser

print("번역할 문장을 입력하시오")
strText = ""; intext = ""
while True:
    print("-> ", end='')
    intext = input()
    if intext == '끝':
        break
    strText = strText + '%0A' + intext

url = "http://translate.google.co.kr/#ko/en" + strText
webbrowser.open(url)
