def shortenToDate(data):
    index=data.find(",")
    data=data[0:index]
    return data


print(shortenToDate("Friday May 2, 7pm"))
    



