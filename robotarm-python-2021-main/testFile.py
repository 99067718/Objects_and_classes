from pygame import Color
from RobotArm import RobotArm
import random
# Let op: hier start het anders voor een random level:
robotArm = RobotArm(f'exercise {random.randint(1,12)}')

# Jouw python instructies zet je vanaf hier:
robotArm.getNextColorRight("red")
    

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()