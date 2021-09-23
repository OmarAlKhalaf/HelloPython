class bcolors:
 HEADER = '\033[95m'
 OKBLUE = '\033[94m'
 OKCYAN = '\033[96m'
 OKGREEN = '\033[92m'
 WARNING = '\033[93m'
 FAIL = '\033[91m'
 ENDC = '\033[0m'
 BOLD = '\033[1m'
 UNDERLINE = '\033[4m'

name = input(bcolors.UNDERLINE + bcolors.HEADER + "Wat is ur name ? : " + bcolors.ENDC)
print(bcolors.OKCYAN + "Hey "+ name +" i heard about new game,it's called the final world." + bcolors.ENDC)
print(bcolors.OKCYAN + """it's about 2 team's 
first is : Human 
second is : Goblens.
First is the human team :They don't have that much of the power but they do have brain and they create a robot's that can easily kill a group of 10 goblens
and second team is ! you guessed it goblean :they have magic and dragons. the dragons are tough to kill but they dont comea in a groups.
it's really good game so what do u say?""" + bcolors.ENDC)
start = input(bcolors.UNDERLINE + bcolors.HEADER + "Do u wanna to try it? yes/no : " + bcolors.ENDC)
if start == "yes":
    print(bcolors.OKCYAN + """Great i know that u will love it as i did
i will bring it today after school. see you later """+ name +bcolors.ENDC)
    print(bcolors.OKCYAN + """you at home now and you are waiting for your friend to arrive.
knok knok !! you opend the door,it's Mike your friend.
Hii Mike i was waiting for you ! did you bring it ? 
Mike say : yes i did here it is,enjoei it and after you finsh let me know.
i will leave now ^_^.""" + bcolors.ENDC)
    print(bcolors.OKCYAN + "you got the game, now lit's start playing." + bcolors.ENDC)
elif start == "no":
    print(bcolors.OKCYAN + "well it's up to " + name + " you see you later " + bcolors.ENDC)
name1 = input(bcolors.UNDERLINE + bcolors.HEADER + "Inter your game name : " + bcolors.ENDC)
print(bcolors.OKCYAN + "Hey "+ name1 +" Welcom to the final world." + bcolors.ENDC)
start2 = input(bcolors.UNDERLINE + bcolors.HEADER + """Choose your side,A : Human B : Goblen
press A or B : """ + bcolors.ENDC)
if start2 == "A" or start2 == "a":
    start3 = input(bcolors.UNDERLINE + bcolors.HEADER + "choose your sex Man or Woman : " + bcolors.ENDC)
    if start3 == "man" or start3 == "Man":
        print(bcolors.OKBLUE + """Welcom to the human world,
you walking in the city and you need to gear up and you see smithy workshop you go in and askd hem that you need to gear up and and he recommend.
Sword with shield, Longsword, Bow and arrow, Dual short swords.
1: Sword woth shild : He have a high Defense but low attack medium speed Difficulty is Easy.
2: Longsowrd : He have a high attack, and he can break armor really fast, but he have slow movement Difficulty is medium.
3: Bow adn arrow : High range and high damage + medium to fast movement but you can't fight in close range and he have low defense Difficulty is high
4: Dual sworads : Short swords medium damage really fast movement he have the same low defense as the bow""" + bcolors.ENDC)
        start4 = input(bcolors.UNDERLINE + bcolors.HEADER + """1: Sword and shield
2: Longsword
3: Bow and arrow
4: Dual swords
Wat do u choose? 1/2/3/4 : """ + bcolors.ENDC)
        if start4 == "1":
            print(bcolors.OKBLUE + "You select Sword and shield"+ bcolors.ENDC)
        elif start4 == "2":
            print(bcolors.OKBLUE +"You select Longsword"+ bcolors.ENDC)
        elif start4 == "3":
            print(bcolors.OKBLUE +"You select Bow and arrow"+ bcolors.ENDC)
        elif start4 == "4":
            print(bcolors.OKBLUE +"You select Dual swords"+ bcolors.ENDC)
        print(bcolors.OKBLUE +"aaaaa "+ name1 + bcolors.ENDC)
    elif start3 ==  "woman" or start3 == "Woman":
        print(bcolors.OKBLUE + "Welcom to the human world " + name1 + """,
you walking in the city and you need to gear up and you see smithy workshop you go in and askd hem that you need to gear up and and he recommend.
Sword with shield, Longsword, Bow and arrow, Dual short swords.
1: Sword woth shild : He have a high Defense but low attack medium speed Difficulty is Easy.
2: Longsowrd : He have a high attack, and he can break armor really fast, but he have slow movement Difficulty is medium.
3: Bow adn arrow : High range and high damage + medium to fast movement but you can't fight in close range and he have low defense Difficulty is high
4: Dual sworads : Short swords medium damage really fast movement he have the same low defense as the bow""" + bcolors.ENDC)
        start4 = input(bcolors.UNDERLINE + bcolors.HEADER + """1: Sword and shield
2: Longsword
3: Bow and arrow
4: Dual swords
Wat do u choose? 1/2/3/4 : """ + bcolors.ENDC)
        if start4 == "1":
            print(bcolors.OKBLUE + "You select Sword and shield"+ bcolors.ENDC)
        elif start4 == "2":
            print(bcolors.OKBLUE +"You select Longsword"+ bcolors.ENDC)
        elif start4 == "3":
            print(bcolors.OKBLUE +"You select Bow and arrow"+ bcolors.ENDC)
        elif start4 == "4":
            print(bcolors.OKBLUE +"You select Dual swords"+ bcolors.ENDC)
        print(bcolors.OKBLUE +"aaaaa "+ name1 + bcolors.ENDC)