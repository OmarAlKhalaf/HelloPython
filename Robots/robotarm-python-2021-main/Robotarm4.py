from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
for q in range(1,4,):
    for w in range(1,3):
        robotArm.grab();
        robotArm.moveRight();
    robotArm.drop();
    for e in range(1,3):
        robotArm.moveLeft();
for a in range(1,3):
    robotArm.moveRight();
    robotArm.grab()
    for s in range(2,3):
        robotArm.moveLeft();
        robotArm.drop()  

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
