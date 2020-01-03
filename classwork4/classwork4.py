list=[]
while True:
    mesage=input("Do you want add one more  ?(y/n): ")
    if mesage=="y":
        number=int(input("enter number: "))
        list.append(number)
    else:
        break
min=list[0]
max=list[0]
for i in list:
    if i>max:
        max=i
    elif i<min:
        min=i
print(f"max={max}, min={min}")
print("\n\n\n")

for i in range(10):
    if i%2==0:
        print(f"{i} is even number")
    elif i%3==0:
        print(f"{i} devided by 3")
    else:
         print(f"{i} another")

print("\n\n\n")
rangee=int(input("enter range: "))
number=1
for i in range(rangee):
    number=number*(i+1)
print(number)

print("\n\n")

while True:
    pasword=input("enter pasword: ")
    if(pasword=="1111"):
        print("hallo")
        break
    else:
        print("pasword is incorect")

print("\n")
while True:
    number=int(input("enter number: "))
    if number<=0:
        break

list=[]
size=int(input("enter size: "))
for i in range(size):
    element=int(input("enter elsement: "))
    if element<=0:
        break
    list.append(element)
print( list)
        
