
num_1 = input("Enter a number: ")
num_2 = input("Enter another number: ")

"""
if num_1 > num_2:
    print(f"{num_1} is greater than {num_2}")
elif num_1 == num_2:
    print(f"{num_1} is equal to {num_2}")
"""

if num_1.isdigit() and num_2.isdigit():
    conv_num1 = int(num_1)
    conv_num2 = int(num_2)

    if conv_num1 > conv_num2:
        print(f"{conv_num1} is greater")
    elif conv_num1 < conv_num2:
        print(f"{conv_num2} is greater")
    else:
        print(f"The Numbers are equal")


else:
    print("Only Numbers are required")