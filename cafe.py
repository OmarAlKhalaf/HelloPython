drenking = input(" do u want to drenk?")
if drenking == "yes":
    what = input("what do u want to drenk?")
    what = input("we have beer, wine, soft")
    if what == "wine":
        age = input("what is ur age?")
        if int(age) >= 18:

            print("u selekt a wine")
        else:
            print("u are to young to buy a wine")
    elif what == "beer":
        age = input("what is ur age?")
        if int(age) >= 18:

            print("u selekt a beer")
        else:
            print("u are to young to buy a beer")
    elif what == "soft":
        print("u selkt soft")
    else:
        print("sorry we dont have that")

