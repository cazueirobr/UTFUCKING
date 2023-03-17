import time

while True:
    time.sleep(10)
    key = open('keylog.txt', 'r')
    print(key.read())