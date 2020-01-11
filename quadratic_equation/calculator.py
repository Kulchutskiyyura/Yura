def check_second_number(second_number):
    for i in second_number:
        if i.isdigit()==False and i!=".":
            break
    else:
        return True
    return False

def find_operators_index(raw_data):
      
    operator_index=None
       
    for i in range(len(raw_data)):
        #print("in for")
            #print(raw_data[i])
            #print(raw_data[i].isdigit())
        #print(i)
        if raw_data[i].isdigit()==False:
                #print("in if")
                if raw_data[i]==".":
                    continue
                elif  not(raw_data[i]=="-" or raw_data[i]=="+" or raw_data[i]=="*" or raw_data[i]=="/" or raw_data[i]=="^"):
                    print("Your  expresion is incorect 1")
                    break
                if i==0 and raw_data[i]!="-":
                    print("Your  expresion is incorect 2")
                    break
                elif i==0 and raw_data[i]=="-":
                    continue
                if i+1==len(raw_data):
                    print("Your  expresion is incorect 3")
                    break
                if raw_data[i+1].isdigit()==False:
                    print("Your  expresion is incorect 4")
                    break
                elif raw_data[i-1].isdigit()==False:
                    print("Your  expresion is incorect 5")
                    break
                if check_second_number(raw_data[i+1:len(raw_data)])==False:
                    print("Your  expresion is incorect 6")
                    break
                                
                operator_index=i
                #print("find")
                break
    else:
        print("your expresion is incorect")
       
    return operator_index

def create_numbers(raw_data,operators_index):
    list_with_data=[]
    list_with_data.append(float(raw_data[0:operators_index]))  
    list_with_data.append(float(raw_data[operators_index+1:len(raw_data)])) 
    list_with_data.append(raw_data[operators_index])
    return list_with_data
      
        
#append(float(raw_data[operators_index+1:len(raw_data)])
def add(list_with_number):
    resultt=list_with_number[0]+list_with_number[1]
    print(f"{list_with_number[0]} {list_with_number[2]} {list_with_number[1]} = {resultt}")
    
    while True:
        message=input("do you whant calculate one more expration? (y/n) :")
        if message=="y":
            return True
        elif message=="n":
            return False
        else:
            print("you write wrong letter")


def multiple(list_with_number):
    resultt=list_with_number[0]*list_with_number[1]
    print(f"{list_with_number[0]} {list_with_number[2]} {list_with_number[1]} = {resultt}")
    while True:
        message=input("do you whant calculate one more expration? (y/n) :")
        if message=="y":
            return True
        elif message=="n":
            return False
        else:
            print("you write wrong letter")

def division (list_with_number):
    resultt=list_with_number[0]/list_with_number[1]
    print(f"{list_with_number[0]} {list_with_number[2]} {list_with_number[1]} = {resultt}")
    while True:
        message=input("do you whant calculate one more expration? (y/n) :")
        if message=="y":
            return True
        elif message=="n":
            return False
        else:
            print("you write wrong letter")

def subtraction (list_with_number):
    resultt=list_with_number[0]-list_with_number[1]
    print(f"{list_with_number[0]} {list_with_number[2]} {list_with_number[1]} = {resultt}")
    while True:
        message=input("do you whant calculate one more expration? (y/n) :")
        if message=="y":
            return True
        elif message=="n":
            return False
        else:
            print("you write wrong letter")
def find_power(list_with_number):
    resultt=list_with_number[0]**list_with_number[1]
    print(f"{list_with_number[0]} {list_with_number[2]} {list_with_number[1]} = {resultt}")
    while True:
        message=input("do you whant calculate one more expration? (y/n) :")
        if message=="y":
            return True
        elif message=="n":
            return False
        else:
            print("you write wrong letter")

def main2 ():
    while True:

        raw_data=""
        operator_index=None
        while True:
            raw_data=input("enter expression: ")
            operator_index=find_operators_index(raw_data)
            if(operator_index!=None):
                break
        list_with_number=create_numbers(raw_data,operator_index)
        check=True
        if list_with_number[2]=="*":
            check=multiple(list_with_number)
        elif  list_with_number[2]=="+":
            check=add(list_with_number)
        elif  list_with_number[2]=="-":
            check=subtraction(list_with_number)
        elif  list_with_number[2]=="/":
            check=division(list_with_number)
        elif  list_with_number[2]=="^":
            check=find_power(list_with_number)
        else:
            print("error")
        if(check==False):
            break
    print("thank you for choosing our calculator")
        
 

#main()

