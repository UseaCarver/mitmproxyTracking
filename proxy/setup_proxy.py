import os

proxy = "127.0.0.1"
port = '8080'

def Proxy_on():
    os.system('networksetup -setwebproxy  Wi-Fi '+proxy+' '+port)
    os.system('networksetup -setsecurewebproxy Wi-Fi '+proxy+' '+port)

Proxy_on()