def counting_sheep(array):
    number_of_sheep=0
    for i in array:
        if(i==False):
            number_of_sheep+=1
    return number_of_sheep

arr=[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
print(counting_sheep(arr))
