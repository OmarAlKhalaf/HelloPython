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
First is the human team :They don't have that much of the power but they do have brain and and they create a robot's that can easily kill a group of 10 goblens
and second team is ! you guessed it goblean :they have magic and dragons. the dragons are tough to kill but they dont comea in a groups.
it's really good game so what do u say?""" + bcolors.ENDC)
start = input(bcolors.UNDERLINE + bcolors.HEADER + "Do u wanna to try it? yes/no : " + bcolors.ENDC)
if start == "yes":
    print(bcolors.OKCYAN + """Great i know that u will love it as i did
i will bring it today after school. see you later """+ name +bcolors.ENDC)
elif start == "no":
    print(bcolors.OKCYAN + "well it's up to " + name + "you see you later " + bcolors.ENDC)
    