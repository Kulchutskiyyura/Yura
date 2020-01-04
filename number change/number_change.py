number=int(input("enter number: "))

product=1
reverse=0
calculation_sistem=10
multiplier=calculation_sistem**(len(str(number))-1)
list_for_number=[]
while number>0:
    product*=number%calculation_sistem
    reverse+=(number%calculation_sistem)*multiplier
    multiplier/=calculation_sistem
    list_for_number.append(number%calculation_sistem)
    number=int(number/10)

for i in range(len(list_for_number)-1):
    for j in range(len(list_for_number)-(i+1)):
        if(list_for_number[j]>list_for_number[j+1]):
            list_for_number[j],list_for_number[j+1]=list_for_number[j+1],list_for_number[j]

reverse=int(reverse)
print(product)
print(reverse)
print(list_for_number)
