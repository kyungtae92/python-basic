import winsound
import time

sound = {'도':523, '레':587, '미':659, '파':698, '솔':783, '라':880, '시':987, '도':1046}
shcool = "솔솔라라솔솔미 솔솔미미레 솔솔라라솔솔미 솔미레미도"

for i in shcool:
    if i == ' ':
        time.sleep(1)
    else:
        winsound.Beep(sound[i], 300)
