from winreg import *
import time
import os
import subprocess


# [HKEY_CURRENT_USER\SOFTWARE\4kdownload.com\4K Video Downloader\Limits]
# "dayDownloadDate"=hex(b):d2,72,dd,5f,00,00,00,00
# "dayDownloadCount"=dword:00000000


Downloader = '"C:\\Program Files\\4KDownload\\4kvideodownloader\\4kvideodownloader.exe"' #32bit
pipe = subprocess.Popen(Downloader, stderr=subprocess.PIPE,  shell=False)
os.system("mode con: lines=2 cols=40")

key = HKEY_CURRENT_USER
subkey = r"SOFTWARE\4kdownload.com\4K Video Downloader\Limits"
registry = CreateKey(key, subkey)
print("working")
temp,dataType = QueryValueEx(registry, "dayDownloadCount")
while True:
	if pipe.poll() == 0 :
		break
	# print(pipe.returncode)
	# print(type(pipe.returncode))
	time.sleep(5)
	dataValue,dataType = QueryValueEx(registry, "dayDownloadCount")
	if dataValue >= 10:
		SetValueEx(registry, "dayDownloadCount",0, REG_DWORD, 00000000)
		print('count 초기화 완료')
	if temp!= dataValue:
		os.system('cls')
		# os.system('clear')
		print(f"current count: {dataValue} 중단시키려면 ctrl+ c 입력")
	temp = dataValue

CloseKey(registry)
