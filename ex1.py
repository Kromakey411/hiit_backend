print("Welcome to Class!")

num_1 = input("Enter a number: ")
num_2 = input("Enter another number: ")
num_3 = input("Enter a third number: ")

conv_num1 = int(num_1)
conv_num2 = int(num_2)
conv_num3 = int(num_3)

the_sum = conv_num1 + conv_num2 + conv_num3
diff = conv_num1 - conv_num2 - conv_num3
prod = conv_num1 * conv_num2 * conv_num3
avg = the_sum / 3

print(f"The Sum of {num_1}, {num_2}, and {num_3} is {the_sum}")
print(f"The Difference of {num_1}, {num_2}, and {num_3} is {diff}")
print(f"The Product of {num_1}, {num_2}, and {num_3} is {prod}")
print(f"The Average of {num_1}, {num_2}, and {num_3} is {avg}")