def enought_space(max_amount,on_bort,wait):
    if(on_bort+wait<=max_amount):
        return 0
    else :
        return on_bort+wait-max_amount

max=int(input("enter max amount of pasanger: "))
on=int(input("enter amount pesenger on botr: "))
wait=int(input("enter amount of people who are wating: "))
zmin=enought_space(max,on,wait)
if(zmin==0):
    print("enought space")
else:
    print(f"we dont have space for{zmin}")
