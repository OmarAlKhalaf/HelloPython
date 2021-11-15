import time
start = input("Als je wil raket te lancering type { go }.")
if start == "go":
    for k in range (30,0,-1):
        time.sleep(1)
        print("lancering in",k)
    k = True
    print("lanceer de raket!!")