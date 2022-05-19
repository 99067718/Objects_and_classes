class ghosts:
    def __init__(self,color,state,startPos,speed):
        self.state = state
        self.color = color
        self.coordinates = startPos
        self.speed = speed
    

class pacperson:
    def __init__(self,lives= 3,speed = 3,startPosition = ""):
        self.lives = lives
        self.coordinates = startPosition
        self.speed = speed
    
    def movement():
        up = "w"
        down = "s"
        right = "d"
        left = "a"

    def powerUp():
        pass

    def grabdots():
        pass

    def respawn():
        pass

inky = ghosts("blue","follow","0,0,0",5)
pinky = ghosts("pink","wander","0,1,0",3)
player = pacperson(3,20,"2,2,2")