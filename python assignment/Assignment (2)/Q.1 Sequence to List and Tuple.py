# Q.1 Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.

numbers = input("Enter a sequence of comma-separated numbers: ")
numbers_list = numbers.split(',')
numbers_tuple = tuple(numbers_list)

print("List:", numbers_list)
print("Tuple:", numbers_tuple)
