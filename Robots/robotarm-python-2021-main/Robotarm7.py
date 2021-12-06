from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:
robotArm.speed=5
for q in range(1,2):
    for e in range(1,8):
        robotArm.moveRight()
        robotArm.grab()
        for w in range(1,9):
            robotArm.moveRight()
        robotArm.drop()
        for r in range(1,10):
            robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
