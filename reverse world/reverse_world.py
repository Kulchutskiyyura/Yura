def reverse_world(string):
    #first_world_index=0
    list_with_separated_word=string.split()
    print(list_with_separated_word)
    new_string=""
    i=len( list_with_separated_word)-1
    while i>=0: 
        #new_string+=list_with_separated_word[i]+" "
        new_string.append(list_with_separated_word[i])
        print(list_with_separated_word[i])
        i-=1
    return new_string


m=reverse_world("   uyu ui or")
listt=list(range(10,0));
print(m)