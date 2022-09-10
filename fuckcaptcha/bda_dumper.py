import base64
import time

from cipher import decrypt

if __name__ == '__main__':
    bda = input("BDA: ")
    ua = input("User Agent: ")
    ts = int(time.time())
    timeframe = ts - ts % 21600
    key = ua + str(timeframe)
    decrypted = decrypt(base64.b64decode(bda).decode('utf-8', errors='ignore'), key)
    print("BDA: " + decrypted.decode('utf-8', errors='ignore'))
