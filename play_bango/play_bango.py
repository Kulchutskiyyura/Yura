def play_banjo(name):
    if name[0]=="r" or name[0]=="R":
        return name + " plays banjo" 
    else:
        return name + " dont plays banjo" 

name=input("enter name: ")
print(play_banjo(name))
