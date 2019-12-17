import re
import sys
from urllib.request import urlopen

def urlopenRead():
    f = urlopen('http://www.hanbit.co.kr/store/books/full_book_list.html')
    bytes_contnet =f.read()
    return bytes_contnet

def urlProcess(bytes_content):
    scanned_text = bytes_content[:1024].decode('ascii', errors='replace')

    match = re.search(r'charset=["\']?([\w-]+)', scanned_text)
    if match:
        encoding = match.group(1)
    else:
        encoding = 'utf-8'
    return encoding

def urlPrint(encoding, bytes_content):
    print('encoding:', encoding, file=sys.stderr)
    text = bytes_content.decode(encoding)
    print(text)

def main():
    bytes_content = urlopenRead()
    encoding = urlProcess(bytes_content)
    urlPrint(encoding, bytes_content)

main()