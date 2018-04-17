import os

def Proxy_off():
    os.system('networksetup -setwebproxystate Wi-Fi off')
    os.system('networksetup -setsecurewebproxystate Wi-Fi off')

Proxy_off()