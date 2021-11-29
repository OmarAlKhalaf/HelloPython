from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
for q in range(1,4):
    for w in range(1,3):
        robotArm.grab();
        robotArm.moveRight()
    robotArm.drop()
    for e in range(1,3):
        robotArm.moveLeft()
for k in range(1):
    for i in range(2):
        robotArm.moveRight()
    robotArm.grab();
    for o in range(1):
        robotArm.moveLeft()
    robotArm.drop()
for k in range(1,3):
    for i in range(1):
        robotArm.moveRight()
    robotArm.grab();
    for o in range(1):
        robotArm.moveLeft()
    robotArm.drop()
    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
    
    #for r in range (1,3):
     #   for m in range (1,2):
    #        robotArm.moveRight();
   #     robotArm.grab()
  #      robotArm.moveLeft()
 #       robotArm.drop()
