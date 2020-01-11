def mybot(number_of_step_reverse,number_of_stick):
    number_of_points=number_of_stick-(4*number_of_step_reverse)
    return number_of_points

def main():
    number_of_stick=21
    number_of_step_reverse=5
    print("game start")
    while(1):
        print("computer make his  step")
        take=mybot(number_of_step_reverse,number_of_stick)
        print (f"he take {take} ")
        number_of_stick-=take
        number_of_step_reverse-=1
        print (f"the score now is {number_of_stick}")
        if(number_of_stick==0):
            print("you lose")
            break
        take=int(input("enter your choice: "))
        while(1):
            if(take>3 or take<1):
                print("your choice is incorect (you can choose only 1 2 or 3)")
                take=int(input("enter your choice: "))
            else:
                break
        number_of_stick-=take
        print (f"the score now is {number_of_stick}")
        if(number_of_stick==0):
           print("you win")
           break

main()



