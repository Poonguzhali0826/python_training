# 1. Take a list, write a Python program to swap the first and last element of the list.
# Examples:
# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

list_of_element = [12, 35, 9, 56, 24]
new_list = []
temp = list_of_element[0]
list_of_element[0] = list_of_element[-1]
list_of_element[-1] = temp
print(list_of_element)


# 2.Remove the Specific Character from the String

# Input: 'Geeks123For123Geeks'
# Output: GeeksForGeeks
# Explanation: In This, we have removed the '123' character from a string.

input_char = 'Geeks123For123Geeks'
substringToRemove = '123'

output = input_char.replace(substringToRemove, '')
print(output)

# 3.Sort Python Dictionaries by Key

# Input:
# {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

# Output: 
# {'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 2}

input_dict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

sorted_dict = dict(sorted(input_dict.items()))

print(sorted_dict)


# 4.Maximum and Minimum 

# Input : set = ([8, 16, 24, 1, 25, 3, 10, 65, 55])
# Output : max is 65

# Input : set = ([4, 12, 10, 9, 4, 13])
# Output : min is 4
numbers = [8, 16, 24, 1, 25, 3, 10, 65, 55]
maximum = max(numbers)
minimum = min(numbers)

print(f"max is {maximum}")
print(f"min is {minimum}")


# 5.write a program to display “Hello” if a number entered by user is a multiple of five, otherwise print “Bye”


number = int(input())
# Check if the number is a multiple of five
if number % 5 == 0:
    print("Hello")
else:
    print("Bye")