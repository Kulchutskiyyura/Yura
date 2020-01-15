def find_sum_of_multiples_3_5(number):
    sum=0
    for i in range(number):
        if(i%3==0):
            sum+=i
            print(i)
        elif(i%5==0):
            sum+=i
            print(i)
    return sum

print(find_sum_of_multiples_3_5(10))
