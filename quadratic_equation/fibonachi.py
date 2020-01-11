def find_fibonachi_number(number):
    if number==0:
        return 0
    if number==1:
        return 1

    return find_fibonachi_number(number-1)+find_fibonachi_number(number-2)


print(find_fibonachi_number(12))

