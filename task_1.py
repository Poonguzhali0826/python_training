# task1
# 1. Need to swap two variables and the output must be swapped variable, I will give two input as numbers and, I need output like they need to be swapped
a = input()
b = input()

temp = a
a = b
b = temp
print ('a value', a)
print('b value', b)

# task2
# 2. Take two strings as input like first name and last name, so we need output of theirs initial like first name and last name initial as an output
first_Name = input()
last_Name = input()
print ('first_Name intial value', first_Name[0])
print('last_Name initial value', last_Name[0])

# task3
# Take a list of numbers as input like some set of numbers, I need output as odd and even numbers in seperate printing statements
arrNumbers = [4,5,6,188,130,420,87,98,150,44]
for i in arrNumbers:
    if(i%2==0):
       print(i , end =" ")
    else:
        print(i, end =" ")


# task4
# I am giving input as a string, so I need the output as same string but without spaces
name_with_space = "I am Poonguzhali"
name_with_space = name_with_space.replace(" ", "")
print("name_without_space", name_with_space)

# task5
# 5. I will give input as two string first string  set of sentence like "I am Thirukumaran" and the second string is one letter
## Output
# If element is present means give printing statement element is present
a = "I am Poonguzhali"
b = input()

if b in a:
    print("element is present")
else:
    print("element is absent")


# def check_word_presence(sentences, target_word):
#     for sentence in sentences:
#         if target_word in sentence:
#             print(f"'{target_word}' is present in the sentence: '{sentence}'")


# # Input strings
# input_sentences = "I am Thirukumaran. How are you? Hello Thirukumaran!"
# target_word = input()

# # Split the input sentences into a list of individual sentences
# sentences = input_sentences.split(". ")

# # Call the function to check word presence
# check_word_presence(sentences, target_word)
