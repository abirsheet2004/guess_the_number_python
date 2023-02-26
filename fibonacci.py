#Write a python program to print Fibonacci series

number_of_fibonacci = int(input("Enter how many fibonacci numbers you want to print : "))

first_number = 0
second_number = 1
sum = 0

for i in range(1,number_of_fibonacci+1):
    print(sum, end = " ")

    first_number=second_number
    second_number=sum
    sum=first_number+second_number