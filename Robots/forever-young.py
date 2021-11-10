start = input("welke tafel wil je ? 1 t/m 10 ")
if start == "1":
    for k in range(1,11):
        print(str(k) + " x 4 = " + str(k*1))
elif start == "2":
    for k in range(1,11):
        print(str(k) + " x 4 = " + str(k*2))
elif start == "3":
    for k in range(1,11):
        print(str(k) + " x 4 = " + str(k*3))