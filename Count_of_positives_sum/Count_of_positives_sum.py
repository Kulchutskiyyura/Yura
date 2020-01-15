def count_positives_add_negatives(array):
    array_with_result=[]
    if(not array):
        return array_with_result
    array_with_result=[0,0]
    for i in array:
        if(i<0):
            array_with_result[1]+=i
        elif(i>0):
            array_with_result[0]+=1
    return  array_with_result





print(count_positives_add_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))