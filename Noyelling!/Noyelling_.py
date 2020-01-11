def filter_words(str):
    str=str.lower()
    str=str.split()
    for i in range(len(str)-1):
        str[i]+=" "
    str="".join(str)
    str=str[0].upper()+str[1:]
    return str

print(filter_words('WoW this   is     REALLY amazing'))


