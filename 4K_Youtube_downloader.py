"""
author : Clazitive Developer
contact : changhyunlyoo@gmail.com
lastmodified: : 2021.02.23
"""
from winreg import *
import time
import os


# [HKEY_CURRENT_USER\SOFTWARE\4kdownload.com\4K Video Downloader\Limits]
# "dayDownloadDate"=hex(b):d2,72,dd,5f,00,00,00,00
# "dayDownloadCount"=dword:00000000

os.system("mode con: lines=2 cols=40")

key = HKEY_CURRENT_USER
subkey = r"SOFTWARE\4kdownload.com\4K Video Downloader\Limits"
registry = CreateKey(key, subkey)
print("working")
print("종료하려면 ctrl + c 눌러주세요")
temp,dataType = QueryValueEx(registry, "dayDownloadCount")
while True:
	dataValue,dataType = QueryValueEx(registry, "dayDownloadCount")
	SetValueEx(registry, "dayDownloadCount",0, REG_DWORD, 00000000)
	time.sleep(5)
CloseKey(registry)
