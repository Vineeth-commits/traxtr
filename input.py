import re

def input_integer():
    flag = True
    input_value = None
    while flag:
        input_value = input("Input a number:")
        match_val = re.match("[-+]?\\d+$", input_value)
        if match_val is None:
            print("Please enter a valid integer.")
        else:
            flag = False
    number = int(input_value)
    return number

def input_decimal():
    flag = True
    input_value = None
    while flag:
        input_value = input("Please input a number:")
        match_val = re.match("[-+]?\\d+([/.]\\d+)?$", input_value)
        if match_val is None:
            print("Please enter a valid decimal number.")
        else:
            flag = False
    number = float(input_value)
    print("The input number is:", number)

