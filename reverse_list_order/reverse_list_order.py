def reverse_list_order(list):
    for i in range(len(list)//2):
        list[i],list[-i-1]=list[-i-1],list[i]
        #print(i)
        #print("d")
    return list

print(reverse_list_order([1,2,3,4,5]))


