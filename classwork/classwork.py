

try:
    number=int(input("enter nymber: "))
    if number%2==0:
        print("парне")
    else:
        print("непарне")
except ValueError:
    print("некоректні дані")

def chack(age):
    if age<=0:
         raise ZeroDivisionError("That is not a positive number!") 

while 1:
    try:
        age = int(input("enter your age: "))
        chack(age)
        if age%2==0:
            print("парне")
        else:
            print("непарне")
    except ZeroDivisionError as e:
         print(e)
    except ValueError:
        print("некоректні дані")
    else:
        break


while 1:
    data=input("enter number: ")
    try:
        firt_number=float(data[0])
        second_number=float(data[2])
        if(data[1]!=","):
            raise ValueError("you should enter , between number")

    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        
       print(e)
    else:
        m=firt_number/second_number
        print(m)
        break
    finally:
        print("good")
         
dict_week={1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
while 1:
    try:
        number=int(input("enter number: "))
        print(dict_week[number])
    except ValueError:
        print("you enter wrong data")
    except KeyError:
        print("your number is out of range")
    else:
        n=input("do you want enter one more number: ")
        if n=="n":
            break


   



