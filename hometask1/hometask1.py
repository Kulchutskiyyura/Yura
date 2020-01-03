def convert_number_to_string(number):
    number=str(number)
    number="'"+number+"'"
    return number


m=convert_number_to_string(5)
print(m)