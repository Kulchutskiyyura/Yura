
i=0

while i<100:
    if i%2==0:
        print(i,end=" ")
    i+=1
else:
    print("the end")
print("\n\n")
for i in range(100):
    if i%2==0:
        print(i,end=" ")
print("\n\n")
for i in range(100):
    if i%2==0:
        continue
    print(i,end=" ")
print("\n\n")
for i in range(100):
    if i%2==1:
        print(i,end=" ")

print("\n\n")
list_for_cheak=[]
while(1):
    number=input("enter number: ")
    if number=="end":
        break
    else:
        list_for_cheak.append(int(number))


for i in list_for_cheak:
    if i%2==1:
        print("we have odd number")
        break
    else:
        print("everything is good")
else:
    print("we dont have odd number")

print("\n\n")
while(1):
    number=input("enter number: ")
    if number=="end":
        break
    else:
        list_for_cheak.append(int(number))

for i in list_for_cheak:
    i=i**2
    print(i)
print(list_for_cheak)

i=0
while i< len(list_for_cheak):
    list_for_cheak[i]=float(list_for_cheak[i])
    i+=1
print(list_for_cheak)

print("\n\n")
my_range=int(input("enter range: "))
c=0
a=0
b=1

for i in range(my_range):
    print(c,end=" ")
    c=a+b
    a=b
    b=c

print("\n\n")
string_list=["one","two","three","four"]
mesege=input("do you want change list? (y\n): ")

if(mesege=="y"):
    for i in range(len(string_list)):
                   information=input("enter information for %d item" %(i+1))
                   string_list[i]=information
for item in string_list:
        print(item,end=" ")    




