from math import pow
from math import pi
from random import randint
from math import sin
number=randint(1,100)
while(1):
    guess=int(input("enter number: "))
    if number>guess:
        print("your number is lower")
    elif guess>number:
        print("your number is greater")
    else:
        print("you win")
        break


def find_circle_square(radius):
    square=pi*pow(radius,2)
    return square
def find_rectangle_square(a_side,b_side):
    return a_side*b_side
def find_triangle_square(a_side,h):
    print(sin(corner),corner)
    return 0.5*h*a_side
mes=input(" what do you whant to calculate cirscle or rectangle or triangle squere (c/r/t)?: ")
if(mes=="c"):
    radius=float(input("enter raius: "))
    resalt=find_circle_square(radius)
    print(resalt)
elif mes=="r":
    a_side=float(input("enter a side: "))
    b_side=float(input("enter b side: "))
    resalt=find_rectangle_square(a_side,b_side)
    print(resalt)
else:
    a_side=float(input("enter a side: "))
    h=float(input("enter b side: "))
    
    resalt=find_triangle_square(a_side,h)
    print(resalt)
