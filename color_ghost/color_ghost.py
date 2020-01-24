from random import choice
color=("white" , "yellow" , "purple"  ,"red")
class Ghost:
    def __init__(self):
        self.color=choice( color)

ghost=Ghost()
print(ghost.color)