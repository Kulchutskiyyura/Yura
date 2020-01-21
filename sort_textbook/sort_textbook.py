def sort_textbooks(list_with_textbooks):
    for i in range(len(list_with_textbooks)-1):
        for j in range(len(list_with_textbooks)-i-1):
            if(list_with_textbooks[j].lower()>list_with_textbooks[j+1].lower()):
                list_with_textbooks[j],list_with_textbooks[j+1]=list_with_textbooks[j+1],list_with_textbooks[j]
    return list_with_textbooks



list_with_textbooks=["B","a","F","cc","Cb"]
print(sort_textbooks(list_with_textbooks))
