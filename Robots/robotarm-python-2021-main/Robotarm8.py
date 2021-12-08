from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
robotArm.speed=2

robotArm.grab()
for q in range(4):
    for w in range(4):
        robotArm.grab()
        for e in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for e in range(5):
            robotArm.moveLeft()
    for w in range(1):
        robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
