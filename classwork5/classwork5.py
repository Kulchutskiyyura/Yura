from math import sin
def function(*args):
    sum=0.0
    for i in args:
        sum+=i
    avarage=sum/len(args)
    return avarage

print(function(4,8,9,6,3.2))

def modul(number):
    if number>=0:
        return number
    else:
        return -number

print(modul(5),modul(-5))

def find_the_biggest(first,second):
    """ this function find the bigest of two number """ 
    if(first>second):
        return first
    else:
        return second

print(find_the_biggest.__doc__)
print(find_the_biggest(4,8))
def find_circle_square(radius):
    square=3.14*radius**2
    return square
def find_rectangle_square(a_side,b_side):
    return a_side*b_side
def find_triangle_square(a_side,b_side,corner):
    print(sin(corner),corner)
    return a_side*b_side*sin(corner)*0.5
mes=input(" what do you whant to calculate cirscle or rectangle or triangle squere (c/r/t)?: ")
if(mes=="c"):
    radius=int(input("enter raius: "))
    resalt=find_circle_square(radius)
    print(resalt)
elif mes=="r":
    a_side=int(input("enter a side: "))
    b_side=int(input("enter b side: "))
    resalt=find_rectangle_square(a_side,b_side)
    print(resalt)
else:
    a_side=int(input("enter a side: "))
    b_side=int(input("enter b side: "))
    corner=int(input("enter b side: "))
    resalt=find_triangle_square(a_side,b_side,corner)
    print(resalt)

def fun(number):
    sum=0
    while number>0:
        sum+=number%10
        number=int(number/10)
    return sum

print(fun(1238))




















