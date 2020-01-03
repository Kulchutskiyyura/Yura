def enought_fuel(kilometres_left,fuel_left):
    if(kilometres_left<=fuel_left*25):
        return True
    else:
        return False


kilometres=int(input("enter way size: "))
fuel=int(input("enter gallons left: "))
if enought_fuel(kilometres,fuel)==True:
    print("it is posible")
else:
    print("it is imposible")
