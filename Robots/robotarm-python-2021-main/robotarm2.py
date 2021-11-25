from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

# Jouw python instructies zet je vanaf hier:
robotArm.grab();
for x in range (1,11):
    robotArm.moveRight();
robotArm.drop();
for q in range(1,6):
    robotArm.moveLeft();
robotArm.grab();
for w in range(5,11):
    robotArm.moveRight();
robotArm.drop();
for e in range(1,3):
    robotArm.moveLeft();
robotArm.grab();
for r in range(3,11):
    robotArm.moveRight();
robotArm.drop();
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
