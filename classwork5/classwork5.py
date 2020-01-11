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

#розвязок квадратного рівнння
from math import sqrt
#from calculator import main2
def check_raw_data(raw_data):
    #print("check")
    counter_of_x=0
    counter_of_sq=0
    reverse_counter_of_sign=2
    if raw_data[0]=="-":
        reverse_counter_of_sign=3
    if raw_data.find("x^2")==-1:
        print("dont find x^2")
        return False
    for i in raw_data:
        if(not(i.isdigit() or i=="x" or i=="^" or i=="+" or i=="-"  or i==".")):
            return False
        if(i=="x"):
            counter_of_x+=1
        elif(i=="^"):
            counter_of_sq+=1
        if i=="+" or i=="-":
            reverse_counter_of_sign-=1

    else:
        if counter_of_x==2  and counter_of_sq==1 and reverse_counter_of_sign==0:
            return True
        else:
            return False
     
def delate_elements(raw_data,index_of_x,last_position,x_coefficient,size_of_x_expresion):
    raw_data= list(raw_data)
    #print(raw_data)
    j=index_of_x-len(x_coefficient)-last_position
    #print(x_coefficient)
    for i in range(index_of_x-len(x_coefficient)-last_position,index_of_x+size_of_x_expresion):
        #print( raw_data[j],j)
        del raw_data[j]
    #print(raw_data)
    raw_data="".join(raw_data)
    return raw_data

def find_number(index_of_x,raw_data):
    x_coefficient=""
    i=index_of_x-1
    while i>=0:
        if raw_data[i].isdigit() or raw_data[i]=="." :
            x_coefficient=raw_data[i]+x_coefficient
        else:
            break
        i-=1
    return x_coefficient

def find_sign(index_of_x,x_coefficient,raw_data,list_with_sign,position_in_sign_list):
    last_position=0
    
    if (index_of_x-len(x_coefficient))==0:
        last_position=0
    elif(not( raw_data[index_of_x-len(x_coefficient)-1]=="+" or raw_data[index_of_x-len(x_coefficient)-1]=="-"  )):
        #print(index_of_x-len(x_coefficient)-1)
        print("your equation is incorect 2")
        return -1
    else:
        list_with_sign[position_in_sign_list]=raw_data[index_of_x-len(x_coefficient)-1]
        last_position=1
    return last_position

def find_coefficient(raw_data):
    raw_data=raw_data.lower()
    if(not(check_raw_data(raw_data))):
        print("your equation is incorect1")
        return None
    list_with_coefficient=[None,None,None]
    list_with_sign=["+","+","+"]
    index_of_x_sq=raw_data.find("x^2")
    size_of_x_expresion=3;
    x_sq_coefficient=find_number(index_of_x_sq,raw_data)

    #print( index_of_x_sq)
    last_position=find_sign(index_of_x_sq,x_sq_coefficient,raw_data,list_with_sign,0)
    #print(last_position)
    
    raw_data=delate_elements(raw_data,index_of_x_sq,last_position,x_sq_coefficient,size_of_x_expresion)
    #print( x_sq_coefficient)
    #print(raw_data)

    size_of_x_expresion=1
    index_of_x=raw_data.find("x")
    x_coefficient=find_number(index_of_x,raw_data)
   # print(x_coefficient,len(x_coefficient),index_of_x)
    last_position=find_sign(index_of_x,x_coefficient,raw_data,list_with_sign,1)
    raw_data=delate_elements(raw_data,index_of_x,last_position,x_coefficient,size_of_x_expresion)
    #print(raw_data)
    
    if(x_sq_coefficient==""):
        list_with_coefficient[0]=1.0
    else:
        list_with_coefficient[0]=float(x_sq_coefficient)
    if x_coefficient=="":
        list_with_coefficient[1]=1.0
    else:
        list_with_coefficient[1]=float(x_coefficient)

    list_with_coefficient[2]=float(raw_data)
    #print(list_with_coefficient)
   # print(list_with_sign)
    for i in range(len(list_with_coefficient)):
        if list_with_sign[i]=="-":
            list_with_coefficient[i]=-list_with_coefficient[i]
    #print(list_with_coefficient)
    return list_with_coefficient



def find_descreminant(list_with_coefficient):
    return (list_with_coefficient[1]**2)-(4*list_with_coefficient[0]*list_with_coefficient[2])

def find_x(list_with_coefficient, descreminant):
    list_with_x=[0,0]
    if(descreminant<0):
        return None
    list_with_x[0]=(-list_with_coefficient[1]+sqrt(descreminant))/(2*list_with_coefficient[0])
    list_with_x[1]=(-list_with_coefficient[1]-sqrt(descreminant))/(2*list_with_coefficient[0])
    return list_with_x
def ham_fun():
    print("ou shit i am sorry)")

def main():
    print("example of expresion:x^2+8x+5 or -8x+5+x^2 or 2+5x+x^2 ; you also can use 'X' instead of 'x' ")
    while True:
        
        raw_data=input("enter your exprasion: ")
        if raw_data=="end":
            break
        #if raw_data=="calculator":
            #print("calculator mod is active")
            #main2()
            #print("calculator mod is off")
            #continue
        if raw_data=="hamno_cod":
            ham_fun()
            continue
        list_with_coefficient=find_coefficient(raw_data)
        if not list_with_coefficient:
            #print("your expresion is incorect")
            continue
        descreminant=find_descreminant(list_with_coefficient)

        print(f"descreminant = {descreminant}")
        if(descreminant<0):
            print("complex number is too difficalt....")
            continue
        list_with_x=find_x(list_with_coefficient, descreminant)
        print (f"x1={list_with_x[0]} x2={list_with_x[1]}")



   

            
                                 

# find_coefficient("x+25+x^2")
main()
#калькулятор



















